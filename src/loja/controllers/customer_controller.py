from src.loja.models.customer import Customer
from src.loja.repositories.customer_dao import CustomerDAO
from src.loja.dtos.address_dto import AddressDTO
from src.loja.converters.address import AddressConverter

class CustomerController:

    def __init__(self, dao: CustomerDAO, converter: AddressConverter):
        self.dao = dao
        self.address_converter = converter

    def new_customer(self, name: str, social_number: str):
        customer = Customer(name, social_number)
        self.dao.persist(customer)

    def add_address(self, id: int, form: AddressDTO): #usamos form de formulario
        customer = self.dao.find_one(id)
        address = self.address_converter.convert(form)
        customer.add_address(address)

    def list(self):
        return self.dao.find_all()

    def show(self, id: int):
        return self.dao.find_one(id)

    def remove(self, id: int):
        return self.dao.remove(id)
