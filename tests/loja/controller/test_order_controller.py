class TestOrderController:

    @pytest.fixture()
    def mock_dao(self):
        return MagicMock()

    @pytest.fixture()
    def controller(self, mock_dao):
        return OrderController(dao=mock_dao)

    def test_should_create_an_order(self, controller, mock_dao):
        form = OrderDTOFactory.create()

        controller.new_order(form)

        assert mock_dao.persist.called

        given_order = mock_dao.persist.call_args.args[0]

