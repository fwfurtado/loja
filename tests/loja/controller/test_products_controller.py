from unittest.mock import MagicMock
import pytest

from src.loja.controllers.products_controller import ProductsController


class TestProductsController:

    @pytest.fixture()
    def mock_dao(self):
        return MagicMock

    def test_should_create_a_new_product(self,mock_dao):
        name = "T-shirt"
        price = 15.00
        photo = "image.png"
        description = "Nike"

        controller = ProductsController(dao=mock_dao)

        controller.new_product(name,price,photo,description)

        assert mock_dao.persist.called
        given_product = mock_dao.persist.call_args.args[0]

        assert given_product.name == name
        assert given_product.price == price
        assert given_product.photo == photo
        assert given_product.description == description