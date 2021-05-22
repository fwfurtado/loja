from typing import List, Optional
from src.loja.models.product import Product
from sqlalchemy.orm import Session


class ProductDAO:  # Criando a rotina que faz a interface para gravar dados no banco de dados
    def __init__(self, session: Session):
        self.__session = session

    def persist(self, product: Product):  # Gravar alguma informação no banco de dados
        if not product.id:
            self.__session.add(product)
        else:
            self.__session.merge(product)

    def find_all(self) -> List[Product]:  # Listar tudo que foi gravado
        return self.__session.query(Product).all()

    def find_one(self, id: int) -> Optional[Product]:  # Lista as informações de 1 ID
        return self.__session.query(Product).filter(Product.id == id).first()

    def remove(self, id: int):  # Remove um ID
        product = self.find_one(id)
        if product:
            self.__session.delete(product)
        else:
            raise ValueError("Produto não localizado")
            # self.__session.query(Product).filter(Product.id == id).delete()
