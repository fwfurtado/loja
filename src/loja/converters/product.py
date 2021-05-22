from src.loja.dtos.product import ProductDTO
from src.loja.models.product import Product


class ProductConverter:
    @staticmethod
    def convert(form: ProductDTO) -> Product:
        return Product(
            name=form.name,
            price=form.price,
            photo=form.photo,
            description=form.description,
        )
