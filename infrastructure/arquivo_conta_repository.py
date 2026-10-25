import json
import os

from application.conta_repository import IContaRepository
from domain.cliente import Cliente
from domain.conta import Conta


class ArquivoContaRepository(IContaRepository):
    def __init__(self, caminho):
        self.caminho = caminho
        pasta = os.path.dirname(caminho)
        if pasta:
            os.makedirs(pasta, exist_ok=True)
        if not os.path.exists(self.caminho):
            with open(self.caminho, "w", encoding="utf-8") as arquivo:
                arquivo.write("")

    def listar(self):
        contas = []
        with open(self.caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    dados = json.loads(linha)
                    cliente = Cliente(dados["cliente"]["nome"], dados["cliente"]["cpf"])
                    contas.append(Conta(
                        dados["numero"], cliente, dados["saldo"], dados.get("historico", [])
                    ))
        return contas

    def buscar(self, numero):
        numero = int(numero)
        for conta in self.listar():
            if conta.numero == numero:
                return conta
        return None

    def salvar(self, conta):
        contas = self.listar()
        atualizadas = [item for item in contas if item.numero != conta.numero]
        atualizadas.append(conta)
        atualizadas.sort(key=lambda item: item.numero)
        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            for item in atualizadas:
                dados = {
                    "numero": item.numero,
                    "cliente": {"nome": item.cliente.nome, "cpf": item.cliente.cpf},
                    "saldo": item.saldo,
                    "historico": item.historico,
                }
                arquivo.write(json.dumps(dados, ensure_ascii=False) + "\n")
