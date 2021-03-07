import factory
from src.loja.models.address import Address


class AddressFactory(factory.Factory):
    class Meta:
        model = Address

    street = factory.Faker('name')
    number = factory.Faker('pyint',positive=True)
    zip_code = factory.Faker('')
    complement = factory.Faker('msisdn')