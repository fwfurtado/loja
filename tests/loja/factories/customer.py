import factory
from src.loja.models.customer import Customer


class CustomerFactory(factory.Factory):
    class Meta:
        model = Customer

    name = factory.Faker('name')
    social_number = factory.Faker('msisdn')