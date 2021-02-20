from src.loja.repositories.product_dao import ProductDAO
from tests.loja.factories.product_factory import ProductFactory


class TestProductDAO:

    def test_should_increment_length(self):
        dao = ProductDAO()
        product = ProductFactory.create()

        assert len(dao.find_all()) == 0

        dao.persist(product)

        assert len(dao.find_all()) == 1

        read_product = dao.find_one(1)

        assert product.name == read_product.name
        assert product.value == read_product.value
