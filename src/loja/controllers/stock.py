from src.loja.models.stock import Stock
from src.loja.models.product import Product
from src.loja.repositories.stock import StockDAO


class StockController:
    def __init__(self, dao: StockDAO):
        self.dao = dao

    def new_product(self, product: Product, quantity: int):
        new = Stock(product, quantity)
        self.dao.persist(new)

    def list(self):
        return self.dao.find_all()

    def show(self, id: int):
        return self.dao.find_one(id)

    def remove(self, id: int):
        return self.dao.remove(id)

    def withdraw(self, id: int, amount: int):
        stock = self.dao.find_one(id)

        if stock:  # Nulo e 0 são avaliados como false. O restante é true
            stock.remove(amount)
