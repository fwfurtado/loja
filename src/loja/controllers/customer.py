from src.loja.models.customer import Customer
from src.loja.repositories.customer import CustomerDAO
from src.loja.dtos.address import AddressDTO
from src.loja.converters.address import AddressConverter


class CustomerController:
    def __init__(self, dao: CustomerDAO, converter: AddressConverter):
        self.dao = dao
        self.address_converter = converter

    def new_customer(self, name: str, social_number: str):
        customer = Customer(name=name, social_number=social_number)
        self.dao.persist(customer)

    def add_address(
        self, customer_id: int, form: AddressDTO
    ):  # usamos form de formulario
        customer = self.dao.find_one(customer_id)

        if not customer:
            raise ValueError("Customer not found")

        address = self.address_converter.convert(form)
        customer.add_address(address)

    def list(self):
        return self.dao.find_all()

    def show(self, customer_id: int):
        return self.dao.find_one(customer_id)

    def remove(self, customer_id: int):
        return self.dao.remove(customer_id)
