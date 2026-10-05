import uuid
from src.domain.client import Client
from datetime import datetime

class Orcamento:
    def __init__(self, client: Client, valor: float, mao_de_obra: float = 0.0):
        if client is None or valor is None:
            raise ValueError("Client e valor não podem ser None") 
        if mao_de_obra < 0:
            raise ValueError("Mão de obra não pode ser negativa")
        self.client = client
        self.valor = valor
        self.status = "pendente"
        self.id = uuid.uuid4()  # Gera um ID único para cada instância de Orcamento
        self.data_criacao = datetime.now() # Armazena a data e hora de criação do orçamento
        self.itens = []  # Lista para armazenar os itens do orçamento
        self.mao_de_obra = mao_de_obra  # Inicializa o valor da mão de obra

    def adicionar_item(self, item):
        self.itens.append(item)  # Adiciona um item à lista de itens do orçamento
