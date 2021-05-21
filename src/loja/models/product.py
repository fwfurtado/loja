from datetime import datetime
from sqlalchemy import Column, BigInteger, String, Numeric, DateTime
from src.loja.infra.database import Base
from typing import Optional


class Product(Base):
    __tablename__ = "products"
    id: Optional[int] = Column(BigInteger, primary_key=True)
    name: str = Column(String, nullable=False)
    price: float = Column(Numeric, nullable=False)
    photo: str = Column(String)
    description: str = Column(String, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now, nullable=False)

    def __str__(self):
        return f"Product({self.name, self.price, self.photo, self.description})"
