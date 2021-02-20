import pytest
from src.loja.models.stock import Stock
from tests.loja.factories.product_factory import ProductFactory


class TestAddProduct:
    def test_should_compute_total_from_items(self):

        t_shirt = ProductFactory.create()

        add1 = Stock(t_shirt, 2)

        assert t_shirt.name == add1.name

        with pytest.raises(ValueError):
            Stock(t_shirt, -2)