import factory
from factory.fuzzy import FuzzyInteger
from src.loja.models.customer import Customer


class CustomerFactory(factory.Factory):
    class Meta:
        model = Customer

    id = FuzzyInteger(low=1)
    name = factory.Faker('name')
    social_number = factory.Faker('msisdn')
