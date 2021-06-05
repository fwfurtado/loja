from typing import List, Optional
from src.loja.models.order import Order
from sqlalchemy.orm import Session
from src.loja.models.order_item import OrderItem
from sqlalchemy.orm.query import Query


class OrderDAO:
    def __init__(self, session: Session):
        self.__session = session

    def persist(self, order: Order):
        if not order.id:
            self.__session.add(order)
        else:
            self.__session.merge(order)

    def find_all(self) -> List[Order]:
        return self.__find_with_join().all()

    def find_one(self, id: int) -> Optional[Order]:
        return self.__find_with_join().filter(Order.id == id).first()

    def remove(self, id: int):
        self.__session.query(Order).filter(Order.id == id).delete()

    def __find_with_join(self) -> Query:
        return self.__session.query(Order).join(
            OrderItem, Order.id == OrderItem.order_id
        )
