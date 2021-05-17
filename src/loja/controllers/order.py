from src.loja.models.order import OrderPaymentType
from src.loja.repositories.order import OrderDAO
from src.loja.dtos.order import OrderDTO
from src.loja.converters.order import OrderConverter
from src.loja.dtos.order import OrderDTO
from src.loja.repositories.order import OrderDAO
from src.loja.infra.payment_client import PaymentClient


class OrderController:
    def __init__(self, dao: OrderDAO, converter: OrderConverter, client: PaymentClient):
        self.dao = dao
        self.converter = converter
        self.client = client

    def new_order(self, form: OrderDTO):
        order = self.converter.convert(form)
        self.dao.persist(order)

    def paid(self, order_id: int):
        order = self.dao.find_one(order_id)

        if not order:
            raise ValueError("Order not found")

        if order.payment_type == OrderPaymentType.BANK_SLIP:
            self.client.create_payment_bank_slip(order=order)
            order.pending()
        else:
            self.client.create_payment_online(order=order)
            order.pending()
            order.paid()

    def list(self):
        return self.dao.find_all()

    def show(self, customer_id: int):
        return self.dao.find_one(customer_id)

    def remove(self, customer_id: int):
        return self.dao.remove(customer_id)
