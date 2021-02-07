from src.loja.models.customer import Customer
from src.loja.repositories.customer_dao import CustomerDAO


class TestCustomerDAO:

    def test_should_increment_length(self):
        dao = CustomerDAO()
        customer = Customer("Fernando", "12342134")

        assert len(dao.find_all()) == 0

        dao.persist(customer)

        assert len(dao.find_all()) == 1

        read_customer = dao.find_one(1)

        assert customer.name == read_customer.name
        assert customer.social_number == read_customer.social_number
