class Address:
    def __init__(self, street: str, number: int, zip_code: str, complement: str):
        if number is not None and number <= 0:
            raise ValueError("Número inválido")
        self.__street = street
        self.__number = number
        self.__zip_code = zip_code
        self.__complement = complement

    @property
    def street(self) -> str:
        return self.__street

    @property
    def number(self) -> int:
        return self.__number

    @property
    def zip_code(self) -> str:
        return self.__zip_code

    @property
    def complement(self) -> str:
        return self.__complement

    def __str__(self):
        return f"Address({self.street, self.number, self.zip_code, self.complement})"
