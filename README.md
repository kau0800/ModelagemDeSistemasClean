# Exercício 3 — Clean Architecture e DIP (Python)

Sistema bancário com cadastro, depósito, saque, consulta e histórico, persistindo as contas em `data/contas.txt`. O núcleo depende da abstração `IContaRepository`, não da implementação em arquivo.

## Executar
Requer Python 3.10 ou superior. Não precisa instalar dependências.

```bash
python main.py
```

O arquivo `data/contas.txt` é criado automaticamente. Cada conta é armazenada como uma linha JSON dentro do TXT, permitindo preservar acentos e os dados do histórico.

## Organização
- `domain/`: entidades e regras centrais.
- `application/`: interface `IContaRepository` e casos de uso.
- `infrastructure/`: implementação em arquivo TXT.
- `presentation/`: interface de terminal.
- `data/`: persistência gerada durante a execução.
