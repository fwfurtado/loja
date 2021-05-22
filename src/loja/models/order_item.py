from typing import Optional
from decimal import Decimal
from src.loja.models.product import Product
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, DateTime, Numeric, Enum as OrmENum
from sqlalchemy.orm import relationship
from src.loja.infra.database import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    product_id = Column(BigInteger, ForeignKey("products.id"))
    product = relationship("Product")
    order_id = Column(BigInteger, ForeignKey("orders.id"))
    amount = Column(Numeric, nullable=True)
    quantity = Column(Integer, nullable=True)

    @property
    def total(self) -> Decimal:
        return self.__amount * self.__quantity
