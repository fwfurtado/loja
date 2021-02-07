from src.loja.models.customer import Customer
from src.loja.repositories.customer_dao import CustomerDAO


class CustomerController:

    def __init__(self, dao: CustomerDAO):
        self.dao = dao

    def new_customer(self, name: str, social_number: str):
        customer = Customer(name, social_number)
        self.dao.persist(customer)

    def list(self):
        return self.dao.find_all()

    def show(self, id: int):
        return self.dao.find_one(id)

    def remove(self, id: int):
        return self.dao.remove(id)
