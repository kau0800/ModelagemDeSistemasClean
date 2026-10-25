class Cliente:
    def __init__(self, nome, cpf):
        nome = nome.strip()
        cpf = cpf.strip()
        if not nome or not cpf:
            raise ValueError("Nome e CPF são obrigatórios.")
        self.nome = nome
        self.cpf = cpf
