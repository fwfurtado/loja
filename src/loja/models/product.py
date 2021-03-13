class Product:

    def __init__(self, name: str, price: float, photo: str, description: str, id: int=None):
        if price <= 0:
            raise ValueError("Preço deve ser maior que zero")
        self.__name = name
        self.__price = price
        self.__photo = photo
        self.__description = description
        self.id = id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def photo(self) -> str:

        return self.__photo

    @property
    def description(self) -> str:
        return self.__description

    def __str__(self):
        return f"Product({self.name,self.price,self.photo,self.description})"
