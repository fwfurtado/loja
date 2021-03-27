from tests.loja.factories.address import AddressFactory
from tests.loja.factories.customer import CustomerFactory


class TestCustomer:

    def test_customer_address(self):
        customer = CustomerFactory.create()
        assert len(customer.addresses) == 0

        address = AddressFactory.create()
        customer.add_address(address)

        assert len(customer.addresses) == 1

        assert customer.addresses[0] == address
