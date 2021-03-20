from src.loja.models.product import Product


class Stock:

    def __init__(self, product: Product, quantity: int):
        if quantity < 0:
            raise ValueError("Quantidade deve ser maior que zero")
        self.__product = product
        self.__quantity = quantity

    @property
    def name(self) -> str:
        return self.__product.name

    @property
    def quantity(self) -> int:
        return self.__quantity

    def remove(self, amount: int):
        if amount > self.__quantity:
            raise ValueError("Quantidade maior do que há no estoque")
        self.__quantity -= amount
