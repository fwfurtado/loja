from loja.models.customer import Customer
from loja.models.order import Order
from loja.models.order_item import OrderItem
from loja.models.product import Product


class TestOrder:

    def test_should_compute_total_from_items(self):
        t_shirt = Product("TShirt", 15)
        shorts = Product("Shorts", 25)

        customer = Customer("Fernando", "12341234")
        order = Order(customer)

        order.add_item(OrderItem(t_shirt, 2))
        order.add_item(OrderItem(shorts, 1))

        assert order.total == 55
