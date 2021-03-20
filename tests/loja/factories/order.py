import factory
from src.loja.models.order import Order
from tests.loja.factories.customer import CustomerFactory
from tests.loja.factories.order_item import OrderItemFactory, OrderItemDTOFactory
from src.loja.dtos.order import OrderDTO
from factory import lazy_attribute, SubFactory
from factory.fuzzy import FuzzyInteger


class OrderFactory(factory.Factory):
    class Meta:
        model = Order

    customer = factory.SubFactory(CustomerFactory)
    id = FuzzyInteger(low=1, high=10)

    # Metodo que servira como uma estrategia para que seja possivel criar uma lista, pois nao é possivel fazer lista com SubFactory
    #@lazy_attribute
    #def items(self):
    #    return OrderItemFactory.create_batch(size=1)


class OrderDTOFactory(factory.Factory):
    class Meta:
        model = OrderDTO

    class Params:  # parameters
        item_params = {}

    customer_id = FuzzyInteger(low=1, high=10)

    @lazy_attribute
    def items(self):
        return OrderItemDTOFactory.create_batch(size=1)
