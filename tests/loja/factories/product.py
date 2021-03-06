import factory
from factory.fuzzy import FuzzyFloat, FuzzyInteger
from src.loja.models.product import Product


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = FuzzyInteger(low=1)
    name = factory.Faker('name')
    price = FuzzyFloat(low=0.5, high=50.2, precision=2)
    photo = factory.Faker('image_url')
    description = factory.Faker('paragraph')
