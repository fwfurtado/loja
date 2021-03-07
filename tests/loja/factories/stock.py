import factory
from src.loja.models.stock import Stock
from tests.loja.factories.product_factory import ProductFactory


class StockFactory(factory.Factory):
    class Meta:
        model = Stock

    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker('pyint', min_value=1)
