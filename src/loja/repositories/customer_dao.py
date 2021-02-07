# Data Access Object
from typing import List, Dict, Optional

from src.loja.models.customer import Customer


class CustomerDAO:

    __DATABASE = dict()
    __INDENTITY = 0

    def persist(self, customer: Customer):
        CustomerDAO.__INDENTITY += 1

        CustomerDAO.__DATABASE[CustomerDAO.__INDENTITY] = customer

    def find_all(self) -> Dict[int, Customer]:
        return CustomerDAO.__DATABASE

    def find_one(self, id: int) -> Optional[Customer]:
        return CustomerDAO.__DATABASE.get(id, None)

    def remove(self, id: int):
        del CustomerDAO.__DATABASE[id]
