# Projeto Integrado (Flask + Docker)

Aplicação web simples em Python/Flask para demonstrar execução local e em container Docker, com registro de acessos em arquivo.

## Funcionalidades

- Endpoint principal em `/`
- Registro de acessos com data/hora em arquivo de log
- Configuração por variáveis de ambiente (`PORT` e `LOG_PATH`)

## Requisitos

- Python 3.10+
- pip
- (Opcional) Docker

## Execução local

1. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
python app.py
```

4. Acesse no navegador:

- http://127.0.0.1:8080

## Variáveis de ambiente

- `PORT`: porta de execução da aplicação (padrão: `8080`)
- `LOG_PATH`: caminho do arquivo de log (padrão: `/app/dados/acessos.txt`)

Exemplo (PowerShell):

```powershell
$env:PORT="8080"
$env:LOG_PATH="./dados/acessos.txt"
python app.py
```

## Execução com Docker

Build da imagem:

```bash
docker build -t projeto-integrado .
```

Execução do container:

```bash
docker run -p 8080:8080 -e PORT=8080 -e LOG_PATH=/app/dados/acessos.txt projeto-integrado
```

## Publicação no GitHub

Antes do push para repositório público:

- Verifique se não há arquivos de ambiente local (como `.venv/`)
- Não inclua segredos/tokens no código
- Revise arquivos de configuração e logs
