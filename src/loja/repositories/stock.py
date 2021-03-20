# Data Access Object
from typing import Dict, Optional
from src.loja.models.stock import Stock


class StockDAO:
    __DATABASE = dict()
    __IDENTITY = 0

    def persist(self, product: Stock):
        StockDAO.__IDENTITY += 1
        StockDAO.__DATABASE[StockDAO.__IDENTITY] = product

    def find_all(self) -> Dict[int, Stock]:
        return StockDAO.__DATABASE

    def find_one(self, id: int) -> Optional[Stock]:
        return StockDAO.__DATABASE.get(id, None)

    def remove(self, id: int):
        del StockDAO.__DATABASE[id]
