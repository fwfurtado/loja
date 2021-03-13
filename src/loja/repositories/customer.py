# Data Access Object
from typing import Dict, Optional

from src.loja.models.customer import Customer


class CustomerDAO:

    __DATABASE = dict()
    __IDENTITY = 0

    def persist(self, customer: Customer):
        CustomerDAO.__IDENTITY += 1
        customer.id = CustomerDAO.__IDENTITY
        CustomerDAO.__DATABASE[CustomerDAO.__IDENTITY] = customer

    def find_all(self) -> Dict[int, Customer]:
        return CustomerDAO.__DATABASE

    def find_one(self, id: int) -> Optional[Customer]:
        return CustomerDAO.__DATABASE.get(id, None)

    def remove(self, id: int):
        del CustomerDAO.__DATABASE[id]
