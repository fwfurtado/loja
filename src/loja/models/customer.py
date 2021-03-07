from src.loja.models.address import Address


class Customer:

    def __init__(self, name: str, social_number: str):
        self.__name = name
        self.__social_number = social_number
        self.__addresses = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def social_number(self) -> str:
        return self.__social_number

    def add_address(self, address: Address):
        self.__addresses.append(address)

    @property
    def addresses(self) -> List[Address]:
        return self.__addresses