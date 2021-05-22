from datetime import datetime
from sqlalchemy import Column, BigInteger, String, Numeric, DateTime
from src.loja.infra.database import Base
from typing import Optional
from decimal import Decimal


class Product(Base):
    __tablename__ = "products"
    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    photo = Column(String)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    def __str__(self):
        return f"Product({self.name, self.price, self.photo, self.description})"
