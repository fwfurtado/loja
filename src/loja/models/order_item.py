from decimal import Decimal

from sqlalchemy import (
    Column,
    BigInteger,
    Integer,
    ForeignKey,
    Numeric,
)
from sqlalchemy.orm import relationship
from src.loja.infra.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.loja.models.product import Product  # noqa: F401


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    product_id = Column(BigInteger, ForeignKey("products.id"), nullable=False)
    product = relationship("Product")
    order_id = Column(BigInteger, ForeignKey("orders.id"), nullable=False)
    amount = Column(Numeric, nullable=False)
    quantity = Column(Integer, nullable=False)

    @property
    def total(self) -> Decimal:
        return self.amount * self.quantity
