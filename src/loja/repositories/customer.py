# Data Access Object
from typing import List, Optional
from src.loja.models.customer import Customer
from sqlalchemy.orm import Session


class CustomerDAO:
    def __init__(self, session: Session):
        self.__session = session

    def persist(self, customer: Customer):
        if not customer.id:
            self.__session.add(customer)
        else:
            self.__session.merge(customer)

    def find_all(self) -> List[Customer]:
        return self.__session.query(Customer).all()

    def find_one(self, id: int) -> Optional[Customer]:
        return self.__session.query(Customer).filter(Customer.id == id).first()

    def remove(self, id: int):
        self.__session.query(Customer).filter(Customer.id == id).delete()
