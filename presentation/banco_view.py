class BancoView:
    def __init__(self, casos_uso):
        self.casos_uso = casos_uso

    def executar(self):
        while True:
            print("\n=== SISTEMA BANCÁRIO — CLEAN ARCHITECTURE ===")
            print("1. Criar conta")
            print("2. Consultar conta")
            print("3. Depositar")
            print("4. Sacar")
            print("5. Ver histórico")
            print("0. Sair")
            opcao = input("Escolha: ").strip()
            try:
                if opcao == "1":
                    nome = input("Nome: ")
                    cpf = input("CPF: ")
                    saldo = self._ler_valor("Saldo inicial: R$ ")
                    conta = self.casos_uso["criar"].executar(nome, cpf, saldo)
                    self._mostrar_conta(conta)
                elif opcao == "2":
                    conta = self.casos_uso["consultar"].executar(self._ler_numero())
                    if conta:
                        self._mostrar_conta(conta)
                    else:
                        print("Conta não encontrada.")
                elif opcao == "3":
                    conta = self.casos_uso["depositar"].executar(
                        self._ler_numero(), self._ler_valor("Valor do depósito: R$ ")
                    )
                    self._mostrar_conta(conta)
                elif opcao == "4":
                    conta = self.casos_uso["sacar"].executar(
                        self._ler_numero(), self._ler_valor("Valor do saque: R$ ")
                    )
                    self._mostrar_conta(conta)
                elif opcao == "5":
                    historico = self.casos_uso["historico"].executar(self._ler_numero())
                    if not historico:
                        print("Ainda não há movimentações.")
                    else:
                        print("\n--- HISTÓRICO ---")
                        for item in historico:
                            print(f'{item["data"]} | {item["tipo"]} | R$ {item["valor"]:.2f} '
                                  f'| Saldo após operação: R$ {item["saldo_apos"]:.2f}')
                elif opcao == "0":
                    print("Até logo!")
                    return
                else:
                    print("Opção inválida.")
            except (ValueError, OSError, KeyError) as erro:
                print(f"Erro: {erro}")

    @staticmethod
    def _ler_numero():
        return int(input("Número da conta: "))

    @staticmethod
    def _ler_valor(prompt):
        return float(input(prompt).replace(",", "."))

    @staticmethod
    def _mostrar_conta(conta):
        print(f"\nConta: {conta.numero}")
        print(f"Cliente: {conta.cliente.nome}")
        print(f"CPF: {conta.cliente.cpf}")
        print(f"Saldo: R$ {conta.saldo:.2f}")
