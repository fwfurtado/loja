import pytest
from src.loja.models.customer import Customer
from src.loja.models.order import Order
from src.loja.models.order import OrderStatus
from src.loja.models.order_item import OrderItem
from tests.loja.factories.order import OrderFactory
from tests.loja.factories.product import ProductFactory


class TestOrder:

    def test_should_compute_total_from_items(self):

        t_shirt = ProductFactory.create(price=15)
        shorts = ProductFactory.create(price=25)

        customer = Customer(name="Fernando", social_number="12341234")
        order = Order(customer=customer)

        order.add_item(OrderItem(product=t_shirt, quantity=2))
        order.add_item(OrderItem(product=shorts, quantity=1))

        assert order.total == 55

    @pytest.mark.skip()
    def test_should_have_default_values(self):
        order = OrderFactory.create()

        assert len(order.items) == 0
        assert order.status == OrderStatus.PENDING

    @pytest.mark.skip()
    def test_should_return_status_paid(self):
        order = OrderFactory.create()
        assert order.status == OrderStatus.PENDING

        order.paid()
        assert order.status == OrderStatus.PAID