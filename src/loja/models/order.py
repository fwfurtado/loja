from datetime import date

from src.loja.models.customer import Customer
from src.loja.models.order_item import OrderItem


class Order:

    def __init__(self, customer: Customer):
        self.__customer = customer
        self.__created_at = date.today()
        self.__items = []

    def add_item(self, item: OrderItem):
        self.__items.append(item)

    @property
    def customer(self) -> Customer:
        return self.__customer

    @property
    def created_at(self) -> date:
        return self.__created_at

    @property
    def total(self) -> float:
        return sum([item.total for item in self.__items])
