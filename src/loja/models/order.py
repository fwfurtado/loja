from datetime import date
from enum import Enum
from typing import List

from src.loja.models.customer import Customer
from src.loja.models.order_item import OrderItem


class OrderStatus(Enum):
    PENDING = 'PENDING'
    PAID = 'PAID'
    SENT = 'SENT'
    RECEIVED = 'RECEIVED'
    CANCELLED = 'CANCELLED'


class Order:

    def __init__(self, customer: Customer):
        self.__customer = customer
        self.__created_at = date.today()
        self.__items = []
        self.__status = OrderStatus.PENDING

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

    @property
    def items(self) -> List[OrderItem]:
        return self.__items

    @property
    def status(self) -> OrderStatus:
        return self.__status
