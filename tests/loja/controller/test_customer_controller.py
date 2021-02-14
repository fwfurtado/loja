from unittest.mock import MagicMock

import pytest
from src.loja.controllers.customer_controller import CustomerController


class TestCustomerController:

    @pytest.fixture()
    def mock_dao(self):
        return MagicMock()

    def test_should_create_a_customer(self, mock_dao):
        name = "Fernando"
        social_number = "12341234"

        controller = CustomerController(dao=mock_dao)

        controller.new_customer(name, social_number)

        assert mock_dao.persist.called
        given_customer = mock_dao.persist.call_args.args[0]

        assert given_customer.name == name
        assert given_customer.social_number == social_number

