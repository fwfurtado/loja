from unittest.mock import MagicMock

import pytest
import random
from src.loja.models.order import OrderStatus
from src.loja.controllers.order import OrderController
from src.loja.converters.order import OrderConverter

from tests.loja.factories.customer import CustomerFactory
from tests.loja.factories.order import OrderDTOFactory, OrderFactory
from tests.loja.factories.product import ProductFactory



class TestOrderController:

    @pytest.fixture()
    def order_dao(self):
        return MagicMock()

    @pytest.fixture()
    def product_dao(self):
        return MagicMock()


    @pytest.fixture()
    def customer_dao(self):
        return MagicMock()

    @pytest.fixture()
    def converter(self, customer_dao, product_dao):
        return OrderConverter(customer_dao, product_dao)

    @pytest.fixture()
    def controller(self, order_dao, converter):
        return OrderController(dao=order_dao, converter=converter)

    def test_should_create_an_order(self, controller, order_dao, product_dao, customer_dao):
        product = ProductFactory.create()
        customer = CustomerFactory.create()
        product_dao.find_one.return_value = product
        customer_dao.find_one.return_value = customer

        form = OrderDTOFactory.create()
        form.customer_id = customer.id
        form.items[0].product_id = product.id

        controller.new_order(form)

        assert order_dao.persist.called

        given_order = order_dao.persist.call_args[0][0]

        assert form.customer_id == given_order.customer.id
        assert len(form.items) == len(given_order.items)

        for form_item, order_item in zip(form.items, given_order.items):
            assert form_item.quantity == order_item.quantity
            assert form_item.product_id == order_item.product_id

    def test_update_status_to_paid(self, controller, order_dao):
        order = OrderFactory.create()
        order_dao.find_one.return_value = order

        controller.paid(order.id)
        assert order.status == OrderStatus.PAID
        assert order_dao.find_one.called