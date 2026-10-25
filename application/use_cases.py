from domain.cliente import Cliente
from domain.conta import Conta


class CriarContaUseCase:
    def __init__(self, repository):
        self.repository = repository

    def executar(self, nome, cpf, saldo_inicial):
        contas = self.repository.listar()
        numero = max((conta.numero for conta in contas), default=0) + 1
        cliente = Cliente(nome, cpf)
        conta = Conta(numero, cliente, float(saldo_inicial))
        self.repository.salvar(conta)
        return conta


class ConsultarContaUseCase:
    def __init__(self, repository):
        self.repository = repository

    def executar(self, numero):
        return self.repository.buscar(numero)


class DepositarUseCase:
    def __init__(self, repository):
        self.repository = repository

    def executar(self, numero, valor):
        conta = self.repository.buscar(numero)
        if conta is None:
            raise ValueError("Conta não encontrada.")
        conta.depositar(valor)
        self.repository.salvar(conta)
        return conta


class RealizarSaqueUseCase:
    def __init__(self, repository):
        # DIP: depende da abstração IContaRepository, não do arquivo TXT.
        self.repository = repository

    def executar(self, numero, valor):
        conta = self.repository.buscar(numero)
        if conta is None:
            raise ValueError("Conta não encontrada.")
        conta.sacar(valor)
        self.repository.salvar(conta)
        return conta


class ConsultarHistoricoUseCase:
    def __init__(self, repository):
        self.repository = repository

    def executar(self, numero):
        conta = self.repository.buscar(numero)
        if conta is None:
            raise ValueError("Conta não encontrada.")
        return conta.historico
