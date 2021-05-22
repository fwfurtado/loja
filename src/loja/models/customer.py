from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from src.loja.infra.database import Base
from src.loja.models.address import Address


class Customer(Base):
    __tablename__ = "customers"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    social_number = Column(String, nullable=True)
    addresses = relationship("Address")

    def add_address(self, address: Address):
        self.addresses.append(address)  # type: ignore
