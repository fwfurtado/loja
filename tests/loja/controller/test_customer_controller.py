from unittest.mock import MagicMock

import pytest
import random
from src.loja.controllers.customer import CustomerController
from src.loja.converters.address import AddressConverter

from tests.loja.factories.customer import CustomerFactory

from tests.loja.factories.address import AddressDTOFactory


class TestCustomerController:

    @pytest.fixture()
    def mock_dao(self):
        return MagicMock()

    @pytest.fixture()
    def controller(self, mock_dao):
        return CustomerController(dao=mock_dao, converter=AddressConverter())

    @pytest.mark.skip()
    def test_should_create_a_customer(self, controller, mock_dao):
        name = "Fernando"
        social_number = "12341234"

        controller.new_customer(name, social_number)

        assert mock_dao.persist.called
        given_customer = mock_dao.persist.call_args.args[0]

        assert given_customer.name == name
        assert given_customer.social_number == social_number

    @pytest.mark.skip()
    def test_should_return_an_empty_list(self, controller, mock_dao):
        assert len(controller.list()) == 0
        assert mock_dao.find_all.called

    @pytest.mark.skip()
    def test_should_return_a_filled_list(self, controller, mock_dao):
        size = random.randint(0, 500)
        list_of_customer = CustomerFactory.create_batch(size)

        mock_dao.find_all.return_value = list_of_customer

        assert len(controller.list()) == size
        assert mock_dao.find_all.called

    @pytest.mark.skip()
    def test_should_add_address_to_customer(self, controller, mock_dao):
        customer = CustomerFactory.create()
        mock_dao.find_one.return_value = customer

        address_form = AddressDTOFactory.create()
        controller.add_address(1,address_form)

        assert len(customer.addresses) == 1

        customer_address = customer.addresses[0]
        assert customer_address.street == address_form.street
        assert customer_address.number == address_form.number
        assert customer_address.zip_code == address_form.zip_code
        assert customer_address.complement == address_form.complement



        
