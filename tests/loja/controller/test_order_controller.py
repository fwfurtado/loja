from unittest.mock import MagicMock

import pytest
import random
from src.loja.controllers.order import OrderController
from src.loja.converters.order import OrderConverter

from tests.loja.factories.customer import CustomerFactory
from tests.loja.factories.order import OrderDTOFactory
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
    def controller(self, order_dao):
        return OrderController(dao=order_dao)

    def test_should_create_an_order(self, controller, order_dao):
        product = ProductFactory.create()
        customer = CustomerFactory.create()

        form = OrderDTOFactory.create()

        controller.new_order(form)

        assert order_dao.persist.called

        given_order = order_dao.persist.call_args.args[0]
