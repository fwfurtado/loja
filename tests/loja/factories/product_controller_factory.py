import factory
from src.loja.controllers.products_controller import ProductsController


class ProductControllerFactory(factory.Factory):
    class Meta:
        model = ProductsController

    name = factory.Faker('name')
    price = factory.Faker('pyfloat')
    photo = factory.Faker('name')
    description = factory.Faker('paragraph')
