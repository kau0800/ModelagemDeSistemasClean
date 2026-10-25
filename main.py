from infrastructure.arquivo_conta_repository import ArquivoContaRepository
from application.use_cases import (
    CriarContaUseCase, ConsultarContaUseCase, DepositarUseCase,
    RealizarSaqueUseCase, ConsultarHistoricoUseCase
)
from presentation.banco_view import BancoView


def main():
    repository = ArquivoContaRepository("data/contas.txt")
    casos_uso = {
        "criar": CriarContaUseCase(repository),
        "consultar": ConsultarContaUseCase(repository),
        "depositar": DepositarUseCase(repository),
        "sacar": RealizarSaqueUseCase(repository),
        "historico": ConsultarHistoricoUseCase(repository),
    }
    BancoView(casos_uso).executar()


if __name__ == "__main__":
    main()
