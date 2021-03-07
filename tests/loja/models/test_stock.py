import pytest
from src.loja.models.stock import Stock
from tests.loja.factories.product_factory import ProductFactory


class TestStock:
    def test_should_raise_error_when_stock_is_negative(self):

        t_shirt = ProductFactory.create()

        stock = Stock(t_shirt, 2)

        assert t_shirt.name == stock.name

        with pytest.raises(ValueError):
            Stock(t_shirt, -2)

    def test_should_decrease_the_quantity_of_stock(self):

        t_shirt = ProductFactory.create()

        stock = Stock(t_shirt, 2)
        assert stock.quantity == 2

        stock.remove(1)
        assert stock.quantity == 1

    def test_should_raise_error_when_the_amount_exceed_quantity(self):
        t_shirt = ProductFactory.create()

        stock = Stock(t_shirt, 2)
        assert stock.quantity == 2

        with pytest.raises(ValueError):
            stock.remove(3)


