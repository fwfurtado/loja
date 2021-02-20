from loja.models.stock import Stock
from loja.models.product import Product
from loja.repositories.stock_dao import StockDAO


class TestAddProductDAO:

    def test_should_increment_length(self):
        dao = StockDAO()
        product = Product("shorts", 15)
        add = Stock(product, 10)

        assert len(dao.find_all()) == 0

        dao.persist(add)

        assert len(dao.find_all()) == 1

        read_addProduct = dao.find_one(1)

        assert add.name == read_addProduct.name
        assert add.quantity == read_addProduct.quantity
