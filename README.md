# ATS10 - Automação de Testes de API Modernas

Projeto desenvolvido para a disciplina de **Análise e Testes de Software (ATS)**.

O objetivo deste exercício é aplicar técnicas de **testes automatizados de APIs**, utilizando Tavern para testes de contrato, testes assíncronos de performance com FastAPI e boas práticas de organização de repositório.

## Tecnologias utilizadas

* Python 3.9+
* Pytest
* Pytest-asyncio
* HTTPX
* Tavern
* FastAPI

## Estrutura do projeto

```text
ATS10/
│
├── api_pagamentos.py
├── test_performance.py
├── test_fluxo_todos.tavern.yaml
├── utils.py
├── .gitignore
└── README.md
```

## Parte 1 - Teste de Contrato com Tavern

Nesta etapa foi utilizado o **Tavern** para testar a API pública JSONPlaceholder.

O teste realiza duas etapas:

1. Busca uma tarefa específica através do endpoint:

```text
GET /todos/{todo_id}
```

2. Obtém todas as tarefas relacionadas ao usuário encontrado:

```text
GET /todos?userId={id_do_usuario}
```

Foram utilizados os seguintes IDs:

* `1`
* `5`
* `15`

O `userId` retornado na primeira requisição é salvo e utilizado na segunda requisição.

Também foi criada a função `validar_lista_tarefas` no arquivo `utils.py`, responsável por verificar se o retorno é uma lista e se pelo menos uma tarefa possui a chave `completed`.

## Parte 2 - Teste de Performance Assíncrona

Nesta etapa foi criada uma API utilizando **FastAPI** com o endpoint:

```text
GET /processar
```

O endpoint simula um processamento de pagamento demorado.

O teste de performance utiliza:

* `pytest`
* `pytest-asyncio`
* `httpx`
* `ASGITransport`
* `asyncio.gather`

Foram testadas chamadas simultâneas de:

* 5 requisições
* 20 requisições
* 50 requisições

O teste verifica se todas as requisições retornam status `200` e se o tempo total de execução permanece abaixo de **3,5 segundos**.

## Parte 3 - .gitignore

Foi criado um arquivo `.gitignore` para impedir que arquivos e diretórios de cache do Python e do Pytest sejam enviados para o repositório.

Entre eles:

```text
__pycache__/
.pytest_cache/
```

Também são ignorados arquivos relacionados a ambientes virtuais e cobertura de testes.

## Instalação

Clone o repositório:

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta:

```bash
cd ATS10
```

Instale as dependências:

```bash
pip install pytest pytest-asyncio httpx tavern fastapi
```

## Executando os testes

Para executar todos os testes:

```bash
python -m pytest
```

### Resultado

O projeto foi testado com sucesso:

```text
6 passed, 1 warning
```

Os 6 testes correspondem a:

* 3 testes do fluxo de tarefas com Tavern;
* 3 testes de performance com 5, 20 e 50 requisições simultâneas.

O aviso apresentado é um `DeprecationWarning` relacionado a uma dependência utilizada pelo Tavern e não representa uma falha nos testes.

## Entregáveis

O exercício possui os seguintes arquivos principais:

* `utils.py`
* `test_fluxo_todos.tavern.yaml`
* `api_pagamentos.py`
* `test_performance.py`
* `.gitignore`
* `README.md`

## Autor

**Carlos Eduardo da Costa Viana**
