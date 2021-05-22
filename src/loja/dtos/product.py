from pydantic import BaseModel
from decimal import Decimal


class ProductDTO(BaseModel):
    name: str
    price: Decimal
    photo: str
    description: str
