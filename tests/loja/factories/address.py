import factory
from src.loja.dtos.address import AddressDTO
from src.loja.models.address import Address


class AddressFactory(factory.Factory):
    class Meta:
        model = Address

    street = factory.Faker('street_name')
    number = factory.Faker('pyint', min_value=1)
    zip_code = factory.Faker('postcode')
    complement = factory.Faker('text')


class AddressDTOFactory(factory.Factory):
    class Meta:
        model = AddressDTO

    street = factory.Faker('street_name')
    number = factory.Faker('pyint', min_value=1)
    zip_code = factory.Faker('postcode')
    complement = factory.Faker('text')
