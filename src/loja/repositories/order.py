from typing import List, Optional
from src.loja.models.order import Order
from sqlalchemy.orm import Session


class OrderDAO:
    def __init__(self, session: Session):
        self.__session = session

    def persist(self, order: Order):
        if not order.id:
            self.__session.add(order)
        else:
            self.__session.merge(order)

    def find_all(self) -> List[Order]:
        return self.__session.query(Order).all()

    def find_one(self, id: int) -> Optional[Order]:
        return self.__session.query(Order).filter(Order.id == id).first()

    def remove(self, id: int):
        self.__session.query(Order).filter(Order.id == id).delete()
