import factory
from src.loja.models.order import Order
from tests.loja.factories.customer_factory import CustomerFactory


class OrderFactory(factory.Factory):
    class Meta:
        model = Order

    customer = factory.SubFactory(CustomerFactory)
