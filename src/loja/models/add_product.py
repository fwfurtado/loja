from src.loja.models.product import Product


class AddProduct:

    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__quantity = quantity

    @property
    def name(self) -> str:
        return self.__product.name

    @property
    def value(self) -> float:
        return self.__product.value

    @property
    def quantity(self) -> int:
        return self.__quantity
