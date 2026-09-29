class Client :
    def __init__(self, nome, telefone=None, observacao=None):
        if nome is None or nome.strip() == "":
            raise ValueError("Nome não pode ser vazio")
        self.nome = nome
        self.telefone = telefone
        self.observacao = observacao 
        
        
