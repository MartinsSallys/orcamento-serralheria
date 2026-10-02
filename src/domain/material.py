import uuid


class Material():
    def __init__(self, name: str, price: float, unidade: str):
        if name is None or unidade is None or unidade.strip() == "" or price < 0 or name.strip() == "":
            raise ValueError("Nome não pode ser None, unidade não pode ser None, preço negativo e nome não pode ser vazio")
        self.name = name
        self.price = price
        self.unidade = unidade
        self.id = uuid.uuid4()  # Gera um ID único para cada instância de Material
        if self.unidade not in ["metros", "centímetros", "milímetros"]:
            raise ValueError("Unidade deve ser 'metros', 'centímetros' ou 'milímetros'")