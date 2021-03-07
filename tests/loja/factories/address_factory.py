import factory
from src.loja.models.address import Address


class AddressFactory(factory.Factory):
    class Meta:
        model = Address

    street = factory.Faker('street_name')
    number = factory.Faker('pyint', min_value=1)
    zip_code = factory.Faker('postcode')
    complement = factory.Faker('text')