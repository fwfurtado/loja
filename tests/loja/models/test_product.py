import pytest
from src.loja.models.product import Product

from tests.loja.factories.product import ProductFactory


class TestProduct:

    def test_product_attribute(self):

        t_shirt = ProductFactory.create()
        with pytest.raises(ValueError):
            Product(t_shirt.name,-t_shirt.price,t_shirt.photo, t_shirt.description)