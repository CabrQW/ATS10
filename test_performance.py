import asyncio
import time

import httpx
import pytest
from httpx import ASGITransport

from api_pagamentos import app


@pytest.mark.asyncio
@pytest.mark.parametrize("quantidade_requisicoes", [5, 20, 50])
async def test_performance(quantidade_requisicoes):
    transport = ASGITransport(app=app)

    async with httpx.AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        inicio = time.perf_counter()

        tarefas = [
            client.get("/processar")
            for _ in range(quantidade_requisicoes)
        ]

        respostas = await asyncio.gather(*tarefas)

        fim = time.perf_counter()

    tempo_total = fim - inicio

    # Todos os status devem ser 200
    assert all(resposta.status_code == 200 for resposta in respostas)

    # Mesmo com 50 requisições, deve levar menos de 3.5 segundos
    assert tempo_total < 3.5