import pytest
from src.domain.client import Client


def test_client_creation():
    client = Client("joão", "123456789", "Observação de teste")
    assert client.nome == "joão"
    assert client.telefone == "123456789"
    assert client.observacao == "Observação de teste"

def test_client_creation_without_telefone_e_observacao():
    client_without_telefone = Client("maria")
    assert client_without_telefone.nome == "maria"
    assert client_without_telefone.telefone is None
    assert client_without_telefone.observacao is None 

def test_client_creation_with_empty_nome():
    with pytest.raises(ValueError):
        Client("")  # Nome vazio deve levantar ValueError

def test_client_creation_with_whitespace_nome():
    with pytest.raises(ValueError):
        Client("   ")  # Nome com apenas espaços deve levantar ValueError

def test_client_creation_with_none_nome():
    with pytest.raises(ValueError):
        Client(None)  # Nome None deve levantar ValueError