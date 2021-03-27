from src.loja.models.product import Product


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__amount = product.price
        self.__quantity = quantity

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def amount(self) -> float:
        return self.__amount

    @property
    def product_name(self) -> str:
        return self.__product.name

    @property
    def product_id(self) -> int:
        return self.__product.id

    @property
    def total(self) -> float:
        return self.__amount * self.__quantity
