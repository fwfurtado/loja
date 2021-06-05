# Data Access Object
from typing import List, Optional
from src.loja.models.stock import Stock
from sqlalchemy.orm import Session


class StockDAO:
    def __init__(self, session: Session):
        self.__session = session

    def persist(self, product: Stock):
        if not product.id:
            self.__session.add(product)
        else:
            self.__session.merge(product)

    def find_all(self) -> List[Stock]:
        return self.__session.query(Stock).all()

    def find_one(self, id: int) -> Optional[Stock]:
        return self.__session.query(Stock).filter(Stock.id == id).first()

    def remove(self, id: int):
        self.__session.query(Stock).filter(Stock.id == id).delete()
