from src.loja.converters.order import OrderConverter
from src.loja.dtos.order import OrderDTO
from src.loja.repositories.order import OrderDAO


class OrderController:
    def __init__(self, dao: OrderDAO, converter: OrderConverter):
        self.dao = dao
        self.converter = converter

    def new_order(self, form: OrderDTO):
        order = self.converter.convert(form)
        self.dao.persist(order)

    def paid(self, order_id: int):
        order = self.dao.find_one(order_id)
        order.paid()

    def list(self):
        return self.dao.find_all()

    def show(self, customer_id: int):
        return self.dao.find_one(customer_id)

    def remove(self, customer_id: int):
        return self.dao.remove(customer_id)
