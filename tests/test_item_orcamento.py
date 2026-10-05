from src.domain.orcamento import Orcamento
from src.domain.item_orcamento import ItemOrcamento
from src.domain.material import Material
from src.domain.client import Client


def test_item_orcamento_creation():
    material = Material("Aço", 100.0, "metros")
    item_orcamento = ItemOrcamento(1.5, material)
    assert item_orcamento.material == material
    assert item_orcamento.quantidade == 1.5

def test_item_orcamento_creation_with_two_items():
    client = Client("Cliente Teste")
    orcamento = Orcamento(client, 1000.0)
    item1 = ItemOrcamento(2.0, Material("Aço", 100.0, "metros"))
    item2 = ItemOrcamento(3.0, Material("Alumínio", 150.0, "metros"))
    orcamento.adicionar_item(item1)
    orcamento.adicionar_item(item2)
    assert len(orcamento.itens) == 2
    assert orcamento.itens[0] == item1
    assert orcamento.itens[1] == item2
