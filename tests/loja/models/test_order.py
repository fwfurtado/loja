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

        customer = Customer("Fernando", "12341234")
        order = Order(customer)

        order.add_item(OrderItem(t_shirt, 2))
        order.add_item(OrderItem(shorts, 1))

        assert order.total == 55

    def test_should_have_default_values(self):
        order = OrderFactory.create()

        assert len(order.items) == 0
        assert order.status == OrderStatus.PENDING

    def test_should_return_status_paid(self):
        order = OrderFactory.create()
        assert order.status == OrderStatus.PENDING

        order = OrderFactory.create(status=OrderStatus.SENT)

        with pytest.raises(ValueError):
            order.paid()

    def test_should_return_status_sent(self):
        order = OrderFactory.create(status=OrderStatus.PAID)
        order.sent()

        assert order.status == OrderStatus.SENT

        with pytest.raises(ValueError):
            order.sent()
