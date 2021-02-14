import factory
from loja.models.product import Product


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('license_plate')
    value = factory.Faker('pyfloat')