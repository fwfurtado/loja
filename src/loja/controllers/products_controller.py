from src.loja.models.product import Product #a confirmar
from src.loja.repositories.customer_dao import ProductDAO #a confirmar

class ProductsController:

    def __init__(self, dao:ProductDAO):
        self.dao = dao

    def new_product(self, name: str, price: float, photo: str, description: str):
        product = Product(name,price,photo,description)
        self.dao.persist(product)

    def list(self):
        return self.dao.find_all()

    def show(self):
        return self.dao.find_one(name) #vai colocar id ou só o nome?

    def remoce(self):
        return self.dao.remove(name)
