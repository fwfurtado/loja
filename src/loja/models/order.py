from datetime import datetime
from enum import Enum

from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, Enum as OrmENum
from sqlalchemy.orm import relationship
from src.loja.infra.database import Base
from src.loja.models.order_item import OrderItem
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.loja.models.customer import Customer  # noqa: F401


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


class Order(Base):
    __tablename__ = "orders"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    customer_id = Column(BigInteger, ForeignKey("customers.id"), nullable=False)
    customer = relationship("Customer")
    payment_type = Column(
        OrmENum(OrderPaymentType), default=OrderPaymentType.BANK_SLIP, nullable=False
    )
    status = Column(OrmENum(OrderStatus), default=OrderStatus.PENDING, nullable=False)
    items = relationship("OrderItem", uselist=True, cascade="save-update")
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    def add_item(self, item: OrderItem):
        item.amount = item.product.price
        self.items.append(item)

    def pending(self):
        if self.status != OrderStatus.CREATED:
            raise ValueError(
                "Atualização inválida. Situação do pedido diferente de CREATED"
            )
        self.status = OrderStatus.PENDING

    def paid(self):
        if self.status != OrderStatus.PENDING:
            raise ValueError(
                "Atualização inválida. Situação do pedido diferente de PENDENTE"
            )
        self.status = OrderStatus.PAID

    @property
    def total(self) -> float:
        return sum([item.total for item in self.items])  # type: ignore
