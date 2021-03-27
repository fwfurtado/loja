from typing import Dict, Optional
from src.loja.models.product import Product


class ProductDAO:  # Criando a rotina que faz a interface para gravar dados no banco de dados
    __DATABASE = dict()  # Dicionário será o nosso banco de dados
    __IDENTITY = 0  # Referente ao ID Ex: Cadastro 1, 2, 3...

    def persist(self, product: Product):  # Gravar alguma informação no banco de dados
        ProductDAO.__IDENTITY += 1  # Acrescentar um ID novo
        product.id = ProductDAO.__IDENTITY
        ProductDAO.__DATABASE[
            ProductDAO.__IDENTITY
        ] = product  # PAssando a informação para o banco de dados

    def find_all(self) -> Dict[int, Product]:  # Listar tudo que foi gravado
        return ProductDAO.__DATABASE

    def find_one(self, id: int) -> Optional[Product]:  # Lista as informações de 1 ID
        return ProductDAO.__DATABASE.get(id, None)

    def remove(self, id: int):  # Remove um ID
        del ProductDAO.__DATABASE[id]
