# Data Access Object
from typing import Dict, Optional
from src.loja.models.stock import Stock

class StockDAO:

    __DATABASE = dict()
    __IDENTITY = 0

    def persist(self, product: Stock):
        AddProductDAO.__IDENTITY += 1
        AddProductDAO.__DATABASE[AddProductDAO.__IDENTITY] = product

    def find_all(self) -> Dict[int, Stock]:
        return AddProductDAO.__DATABASE

    def find_one(self, id: int) -> Optional[Stock]:
        return AddProductDAO.__DATABASE.get(id, None)

    def remove(self, id: int):
        del AddProductDAO.__DATABASE[id]