from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from src.loja.models.product import Product
from src.loja.infra.database import Base

class Stock(Base):
    __tablename__ = "product_stock"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    quantity = Column(BigInteger, nullable=False)
    product_id = Column(BigInteger, ForeignKey("products.id"))
    product = relationship("Product")



    def remove(self, amount: int):
        if amount > self.quantity:
            raise ValueError("Quantidade maior do que há no estoque")
        self.quantity -= amount
