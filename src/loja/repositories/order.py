from typing import Dict, Optional

from src.loja.models.order import Order


class OrderDAO:
    __DATABASE = dict()
    __IDENTITY = 0

    def persist(self, order: Order):
        OrderDAO.__IDENTITY += 1
        order.id = OrderDAO.__IDENTITY
        OrderDAO.__DATABASE[OrderDAO.__IDENTITY] = order

    def find_all(self) -> Dict[int, Order]:
        return OrderDAO.__DATABASE

    def find_one(self, id: int) -> Optional[Order]:
        return OrderDAO.__DATABASE.get(id, None)

    def remove(self, id: int):
        del OrderDAO.__DATABASE[id]
