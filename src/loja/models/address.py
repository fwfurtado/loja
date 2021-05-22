from sqlalchemy import Column, String, Integer, BigInteger, ForeignKey
from src.loja.infra.database import Base


class Address(Base):
    __tablename__ = "customer_addresses"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    street = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    zip_code = Column(String, nullable=False)
    complement = Column(String)
    customer_id = Column(BigInteger, ForeignKey("customers.id"), nullable=False)
