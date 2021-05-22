import pytest
from src.loja.models.product import Product

from tests.loja.factories.product import ProductFactory


class TestProduct:
    @pytest.mark.skip()
    def test_product_attribute(self):

        t_shirt = ProductFactory.create()
        with pytest.raises(ValueError):
            Product(name=t_shirt.name,price=-t_shirt.price,photo=t_shirt.photo, description=t_shirt.description)