import pytest
from loja.models.customer import Customer
from loja.models.order import Order
from loja.models.order_item import OrderItem
from loja.models.product import Product

from tests.loja.factories.product_factory import ProductFactory


class TestProduct:

    def test_product_attribute(self):

        t_shirt = ProductFactory.create(price=15)
        with pytest.raises(ValueError):
            Product(t_shirt.name,-1,t_shirt.photo, t_shirt.description)