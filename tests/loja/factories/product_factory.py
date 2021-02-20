import factory
from src.loja.models.product import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('name')
    price = factory.Faker('pyfloat',positive=True)
    photo = factory.Faker('image_url')
    description = factory.Faker('paragraph')
