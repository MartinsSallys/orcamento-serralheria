import pytest 

from src.domain.material import Material

def test_material_creation():
    material = Material("Aço", 100.0, "metros")
    assert material.name == "Aço"
    assert material.price == 100.0
    assert material.unidade == "metros"  

def test_material_creation_without_unidade():
    with pytest.raises(ValueError):
        Material("Aço", 150.0, None)  # Unidade None deve levantar ValueError

def test_material_creation_with_price_zero():
    material = Material("Alumínio", 0.0, "metros")
    assert material.name == "Alumínio"
    assert material.price == 0.0
    assert material.unidade == "metros"  

def test_material_creations_without_name():
    with pytest.raises(ValueError):
        Material(None, 50.0, "metros")  # Nome None deve levantar ValueError

def test_material_creation_empty_unidade():
    with pytest.raises(ValueError):
        Material("Cobre", 50.0, "")  # Unidade vazia deve levantar ValueError

def test_material_creation_with_empty_name():
    with pytest.raises(ValueError):
        Material("", 50.0, "metros")  # Nome vazio deve levantar ValueError

def test_material_creation_with_spaces_name():
    with pytest.raises(ValueError):
        Material("   ", 50.0, "metros")  # Nome com apenas espaços deve levantar ValueError

def test_material_creation_with_negative_price():
    with pytest.raises(ValueError):
        Material("Cobre", -10.0, "metros")  # Preço negativo deve levantar ValueError

