from src.domain.material import Material

class ItemOrcamento:
    def __init__(self, quantidade: float, material: Material):
        self.material = material
        self.quantidade = quantidade
        
       