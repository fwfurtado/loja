from src.loja.models.product import Product #a confirmar
from src.loja.repositories.customer_dao import ProductDAO #a confirmar

class ProductsController:

    def __init__(self, dao:ProductDAO):
        self.dao = dao

    def new_product(self, name: str, price: float, photo: str, description: str):
        product = Product(name,price,photo,description)
        self.dao.persist(product)

    def list(self): #lista dos produtos já cadastrados
        return self.dao.find_all()

    def show(self,id:int):
        return self.dao.find_one(id)

    def remove(self,id:int):
        return self.dao.remove(id)
