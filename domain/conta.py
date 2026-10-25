from datetime import datetime


class Conta:
    def __init__(self, numero, cliente, saldo=0.0, historico=None):
        if saldo < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self.numero = int(numero)
        self.cliente = cliente
        self.saldo = float(saldo)
        self.historico = list(historico or [])

    def depositar(self, valor):
        valor = float(valor)
        if valor <= 0:
            raise ValueError("O depósito deve ser maior que zero.")
        self.saldo += valor
        self._registrar("Depósito", valor)

    def sacar(self, valor):
        valor = float(valor)
        if valor <= 0:
            raise ValueError("O saque deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor
        self._registrar("Saque", valor)

    def _registrar(self, tipo, valor):
        self.historico.append({
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "tipo": tipo,
            "valor": round(valor, 2),
            "saldo_apos": round(self.saldo, 2),
        })
