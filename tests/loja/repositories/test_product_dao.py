import pytest
from src.loja.repositories.product import ProductDAO
from tests.loja.factories.product import ProductFactory


class TestProductDAO:
    @pytest.mark.skip()
    def test_should_increment_length(self):
        dao = ProductDAO()
        product = ProductFactory.create()

        assert len(dao.find_all()) == 0

        dao.persist(product)

        assert len(dao.find_all()) == 1

        read_product = dao.find_one(1)

        assert product.name == read_product.name
        assert product.price == read_product.price
        assert product.photo == read_product.photo
        assert product.description == read_product.description

