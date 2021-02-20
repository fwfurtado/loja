from unittest.mock import MagicMock

import pytest
from loja.models.product import Product
from src.loja.controllers.stock_controller import StockController


class TestAddProductController:

    @pytest.fixture()
    def mock_dao(self):
        return MagicMock()

    def test_should_create_an_add_product(self, mock_dao):
        product = Product("shorts", 15)
        quantity = 10

        controller = StockController(dao=mock_dao)

        controller.new_product(product, quantity)

        assert mock_dao.persist.called
        given_product = mock_dao.persist.call_args.args[0]

        assert given_product.name == product
        assert given_product.social_number == quantity

