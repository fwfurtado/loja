from src.loja.models.order import Order
from src.loja.repositories.order import OrderDAO
from src.loja.dtos.address import OrderDTO


class OrderController:

    def __init__(self, dao: OrderDAO):
        self.dao = dao

    def new_order(self, form: OrderDTO):
        order = Order()
        self.dao.persist(customer)

    def add_address(self, customer_id: int, form: AddressDTO):  # usamos form de formulario
        customer = self.dao.find_one(customer_id)
        address = self.address_converter.convert(form)
        customer.add_address(address)

    def list(self):
        return self.dao.find_all()

    def show(self, customer_id: int):
        return self.dao.find_one(customer_id)

    def remove(self, customer_id: int):
        return self.dao.remove(customer_id)