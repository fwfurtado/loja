
from src.loja.repositories.customer import CustomerDAO
from tests.loja.factories.customer import CustomerFactory


class TestCustomerDAO:

    def test_should_increment_length(self): # Método = Função dentro de uma classe
        dao = CustomerDAO() # Cria instância do DAO
        customer = CustomerFactory.create()

        assert len(dao.find_all()) == 0 # Garantir que o len de (x) seja ==0

        dao.persist(customer) # Adiciona um cliente no banco de dados

        assert len(dao.find_all()) == 1 # Garante que o len de (x) seja 1, pois já temos um cliente no banco

        read_customer = dao.find_one(1) # Procura pelo cliente que tenha o ID = a 1

        assert customer.name == read_customer.name
        assert customer.social_number == read_customer.social_number
