from src.loja.dtos.order import OrderDTO, OrderItemDTO
from src.loja.models.order import Order
from src.loja.models.order_item import OrderItem
from src.loja.repositories.customer import CustomerDAO
from src.loja.repositories.product import ProductDAO


class OrderConverter:
    def __init__(self, customer_dao: CustomerDAO, product_dao: ProductDAO):
        self.__customer_dao = customer_dao
        self.__product_dao = product_dao

    def convert(self, form: OrderDTO) -> Order:
        customer = self.__customer_dao.find_one(form.customer_id)
        if not customer:
            raise ValueError("Customer not found")

        order = Order(customer=customer)
        for item_dto in form.items:
            item = self.__to_order_item(item_dto)
            order.add_item(item)
        return order

    def __to_order_item(self, form: OrderItemDTO) -> OrderItem:
        product = self.__product_dao.find_one(form.product_id)

        if not product:
            raise ValueError("Product not found")

        return OrderItem(product=product, quantity=form.quantity)
