class Material():
    def __init__(self, name: str, price: float, unidade: str):
        if name is None or unidade is None or unidade.strip() == "" or price < 0 or name.strip() == "":
            raise ValueError("Nome não pode ser None, unidade não pode ser None, preço negativo e nome não pode ser vazio")
        self.name = name
        self.price = price
        self.unidade = unidade
