import factory
from loja.models.product import Product


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('name')
    price = factory.Faker('pyfloat')
    photo = factory.Faker('image_url')
    description = factory.Faker('paragraph')