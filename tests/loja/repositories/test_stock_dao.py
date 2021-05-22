import pytest

from src.loja.models.stock import Stock
from src.loja.repositories.stock import StockDAO

from tests.loja.factories.product import ProductFactory


class TestAddProductDAO:
    @pytest.mark.skip()
    def test_should_increment_length(self):
        dao = StockDAO()
        product = ProductFactory.create()
        add = Stock(product, 10)

        assert len(dao.find_all()) == 0

        dao.persist(add)

        assert len(dao.find_all()) == 1

        read_addProduct = dao.find_one(1)

        assert add.name == read_addProduct.name
        assert add.quantity == read_addProduct.quantity
