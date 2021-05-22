from src.loja.dtos.product import ProductDTO
from src.loja.repositories.product import ProductDAO
from src.loja.converters.product import ProductConverter


class ProductController:
    def __init__(self, dao: ProductDAO, converter: ProductConverter):
        self.dao = dao
        self.converter = converter

    def new_product(self, dto: ProductDTO):
        product = self.converter.convert(dto)
        self.dao.persist(product)

    def list(self):
        return self.dao.find_all()

    def show(self, id: int):
        return self.dao.find_one(id)

    def remove(self, id: int):
        return self.dao.remove(id)
