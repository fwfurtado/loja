from random import randint
from unittest.mock import MagicMock

import pytest
from loja.models.product import Product
from src.loja.controllers.stock import StockController

from tests.loja.factories.product import ProductFactory
from tests.loja.factories.stock import StockFactory

class TestStockController:

    @pytest.fixture()
    def mock_dao(self):
        return MagicMock()

    @pytest.fixture()
    def controller(self, mock_dao):
        return StockController(dao=mock_dao)

    def test_should_create_a_stock(self, mock_dao):
        product = ProductFactory.create()
        quantity = randint(1, 10)

        controller = StockController(dao=mock_dao)

        controller.new_product(product, quantity)

        assert mock_dao.persist.called
        given_product = mock_dao.persist.call_args.args[0]

        assert given_product.name == product.name
        assert given_product.quantity == quantity

    def test_should_return_an_empty_list(self, controller, mock_dao):
        assert len(controller.list()) == 0
        assert mock_dao.find_all.called

    def test_should_decrease_quantity_stock(self, controller, mock_dao):
        amount = randint(1, 10)
        stock = StockFactory.create(quantity=amount)

        mock_dao.find_one.return_value = stock

        controller.withdraw(1, amount-1)
        assert stock.quantity == 1
