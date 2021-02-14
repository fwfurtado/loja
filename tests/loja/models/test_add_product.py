
from src.loja.models.add_product import AddProduct
from tests.loja.factories.product_factory import ProductFactory


class TestAddProduct:
    def test_should_compute_total_from_items(self):

        t_shirt = ProductFactory.create(value=15)

        add1 = AddProduct(t_shirt, 2)

        assert t_shirt.name == add1.name
