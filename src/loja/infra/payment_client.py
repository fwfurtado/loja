import requests
from src.loja.infra.settings import GLOBAL_CONFIG
from src.loja.models.order import Order


class PaymentClient:
    def __init__(self):
        self.settings = GLOBAL_CONFIG.payment
        self.token = self.settings.payment_token or ""

    def login_client(self):
        payload = {
            "username": self.settings.payment_username,
            "password": self.settings.payment_password,
        }
        response = requests.post(f"{self.settings.base_url}/oauth/token", data=payload)

        if response.ok:
            response_body = response.json()
            self.token = (
                f"{response_body['token_type']} {response_body['access_token']}"
            )
        else:
            raise ValueError("Não foi possível fazer login")

    def create_payment_bank_slip(self, order: Order):
        payload = {
            "amount": order.total,
            "ref": str(order.id),
            "callback": None,
        }  # callback é optional
        headers = {"Authorization": self.token}
        response = requests.post(
            f"{self.settings.base_url}/payments/", json=payload, headers=headers
        )

        if not response.ok:
            raise ValueError("Não foi possível realizar pagamento")

    def create_payment_online(self, order: Order):
        payload = {
            "amount": order.total,
            "ref": str(order.id),
            "callback": None,
        }  # callback é optional
        headers = {"Authorization": self.token}
        response = requests.post(
            f"{self.settings.base_url}/payments/online", json=payload, headers=headers
        )

        if not response.ok:
            raise ValueError("Não foi possível realizar pagamento")
