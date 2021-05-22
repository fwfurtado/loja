from sqlalchemy import Column, String, Integer, BigInteger, ForeignKey
from src.loja.infra.database import Base

class Address(Base):
    __tablename__ = "customer_addresses"

    id = Column(BigInteger, primary_key=True)
    street = Column(String, nullable=True)
    number = Column(Integer, nullable=True)
    zip_code = Column(String, nullable=True)
    complement = Column(String)
    customer_id = Column(BigInteger, ForeignKey("customers.id"))