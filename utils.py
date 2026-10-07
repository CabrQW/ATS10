def validar_lista_tarefas(response):
    dados = response.json()

    assert isinstance(dados, list), "O retorno não é uma lista"

    assert any("completed" in tarefa for tarefa in dados), (
        "Nenhuma tarefa possui a chave 'completed'"
    )