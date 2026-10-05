from datetime import datetime

import pytest


from src.domain.orcamento import Orcamento
from src.domain.client import Client

def test_orcamento_creation():
    client = Client("Cliente Exemplo")
    valor = 1000.0
    orcamento = Orcamento(client, valor)
    assert orcamento.client == client
    assert orcamento.valor == valor

def test_orcamento_creation_with_none_client():
    valor = 1000.0
    with pytest.raises(ValueError):
        Orcamento(None, valor)  # Client None deve levantar ValueError

def test_orcamento_creation_with_pedent_value():
    client = Client("Cliente Exemplo")
    valor = 1000.0
    orcamento = Orcamento(client, valor)
    assert orcamento.client == client
    assert orcamento.valor == valor
    assert orcamento.status == "pendente"  # Status deve ser "pendente" por padrão
    assert orcamento.id is not None  # ID deve ser gerado e não deve ser None
    assert isinstance (orcamento.data_criacao, datetime)  # Verifica se data_criacao é uma instância de datetime

def test_orcamento_creation_with_id_uniqueness():
    client1 = Client("Cliente 1")
    assert Orcamento(client1, 1000.0).id != Orcamento(client1,1000.0).id  # IDs devem ser únicos

def test_registry_data_e_hora_():
    before_creation = datetime.now()  # Armazena a data e hora antes da criação do orçamento
    orcamento = Orcamento(Client("Cliente Teste"), 500.0)
    after_creation = datetime.now()  # Armazena a data e hora após a criação do orçamento
    assert isinstance(orcamento.data_criacao, datetime)  # Verifica se data_criacao é uma instância de datetime
    assert before_creation <= orcamento.data_criacao <= after_creation  # Verifica se a data de criação é anterior ou igual à data atual,

def test_orcamento_creation_empty_itens():
    client = Client("Cliente Exemplo")
    valor = 1000.0
    orcamento = Orcamento(client, valor)
    assert orcamento.itens == []  # A lista de itens deve estar vazia por padrão
    assert orcamento.mao_de_obra == 0.0  # O valor da mão de obra deve ser 0.0 por padrão

def test_orcamento_creation_with_mao_de_obra():
    client = Client("Cliente Exemplo")
    valor = 1000.0
    mao_de_obra = 350.0
    orcamento = Orcamento(client, valor, mao_de_obra)
    assert orcamento.client == client
    assert orcamento.valor == valor
    assert orcamento.mao_de_obra == mao_de_obra  # Verifica se o valor da mão de obra foi atribuído corretamente

def test_orcamento_with_mao_de_obra_negative():
    client = Client("Cliente Exemplo")
    with pytest.raises(ValueError):
        Orcamento(client, 1000.0, mao_de_obra=-50.0)  # Levanta ValueError se a mão de obra for negativa
    
   
    