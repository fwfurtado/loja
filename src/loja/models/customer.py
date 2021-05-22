from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from src.loja.infra.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    social_number = Column(String, nullable=True)
    addresses = relationship("Address")

