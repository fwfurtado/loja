import pytest
from loja.models.product import Product

from tests.loja.factories.product_factory import ProductFactory


class TestCustomer:

    def test_customer_address(self):
        customer = CustomerFactory.create()
        assert len(customer.addresses) == 0

        address = AddressFactory.create()
        customer.add_address(address)

        assert len(customer.addresses) == 1

        assert customer.addresses[0] == address
