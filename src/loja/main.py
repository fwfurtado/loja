from src.loja.controllers.customer_controller import CustomerController
from src.loja.repositories.customer_dao import CustomerDAO


def test():
    name = "Fernando"
    cpf = "13241234"

    dao = CustomerDAO()
    controller = CustomerController(dao)

    assert len(controller.list()) == 0

    controller.new_customer(name, cpf)

    assert len(controller.list()) == 1

    customer = controller.show(1)

    assert customer.name == name
    assert customer.social_number == cpf

    print(f"Customer {customer.name} - {customer.social_number}")





if __name__ == '__main__':
    test()