from src.loja.models.product import Product


class AddProduct:

    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__quantity = quantity

    @property
    def name(self) -> Product:
        return self.__product

    @property
    def quantity(self) -> int:
        return self.__quantity
