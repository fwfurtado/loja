from datetime import date
from enum import Enum
from typing import List, Union
from decimal import Decimal

from src.loja.models.customer import Customer
from src.loja.models.order_item import OrderItem


class OrderStatus(Enum):
    CREATED = "CREATED"
    PENDING = "PENDING"
    PAID = "PAID"
    SENT = "SENT"
    RECEIVED = "RECEIVED"
    CANCELLED = "CANCELLED"


class OrderPaymentType(Enum):
    ONLINE = "ONLINE"
    BANK_SLIP = "BANK_SLIP"


class Order:
    def __init__(
        self,
        customer: Customer,
        id: int = None,
        payment_type: OrderPaymentType = OrderPaymentType.BANK_SLIP,
    ):
        self.__customer = customer
        self.__created_at = date.today()
        self.__items: List[OrderItem] = []
        self.__status = OrderStatus.PENDING
        self.id = id
        self.payment_type = payment_type

    def add_item(self, item: OrderItem):
        self.__items.append(item)

    def pending(self):
        if self.__status != OrderStatus.CREATED:
            raise ValueError(
                "Atualização inválida. Situação do pedido diferente de CREATED"
            )
        self.__status = OrderStatus.PENDING

    def paid(self):
        if self.__status != OrderStatus.PENDING:
            raise ValueError(
                "Atualização inválida. Situação do pedido diferente de PENDENTE"
            )
        self.__status = OrderStatus.PAID

    @property
    def customer(self) -> Customer:
        return self.__customer

    @property
    def created_at(self) -> date:
        return self.__created_at

    @property
    def total(self) -> Union[Decimal, int]:
        return sum([item.total for item in self.__items])

    @property
    def items(self) -> List[OrderItem]:
        return self.__items

    @property
    def status(self) -> OrderStatus:
        return self.__status
