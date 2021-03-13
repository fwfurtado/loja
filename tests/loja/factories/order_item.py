import factory
from factory.fuzzy import FuzzyInteger
from src.loja.models.order_item import OrderItem
from src.loja.dtos.order import OrderItemDTO
from tests.loja.factories.product import ProductFactory


class OrderItemFactory(factory.Factory):
    class Meta:
        model = OrderItem

    product = factory.SubFactory(ProductFactory)
    quantity = FuzzyInteger(low=20, high=100)


class OrderItemDTOFactory(factory.Factory):
    class Meta:
        model = OrderItemDTO

    product_id = FuzzyInteger(low=1, high=100)
    quantity = FuzzyInteger(low=20, high=100)
