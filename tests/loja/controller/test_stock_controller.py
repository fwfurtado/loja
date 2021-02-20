from random import randint
from unittest.mock import MagicMock

import pytest
from loja.models.product import Product
from src.loja.controllers.stock_controller import StockController

from tests.loja.factories.product_factory import ProductFactory


class TestAddProductController:

    @pytest.fixture()
    def mock_dao(self):
        return MagicMock()

    @pytest.fixture()
    def controller(self, mock_dao):
        return StockController(dao=mock_dao)

    def test_should_create_an_add_product(self, mock_dao):
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

    def test_should_return_a_filled_list(self, controller, mock_dao):
        size = randint(0, 500)
        list_of_customer = ProductFactory.create_batch(size)

        mock_dao.find_all.return_value = list_of_customer

        assert len(controller.list()) == size
        assert mock_dao.find_all.called
