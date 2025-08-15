# tests/test_api_master.py
import pytest
import allure
from utils.api_client import APIClient
from tests.schemas import PostSchema

client = APIClient("https://jsonplaceholder.typicode.com")

# ----------------------------
# Testes GET parametrizados
# ----------------------------
@allure.feature("API - GET Endpoints")
@pytest.mark.parametrize("endpoint, expected_count", [
    ("/posts", 100),
    ("/comments", 500),
    ("/albums", 100)
])
def test_get_endpoints(endpoint, expected_count):
    with allure.step(f"Requisição GET para {endpoint}"):
        response = client.get(endpoint)
        assert response.status_code == 200

    with allure.step("Validar resposta e quantidade de itens"):
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == expected_count

# ----------------------------
# Testes POST com validação de schema
# ----------------------------
@allure.feature("API - POST")
@allure.story("Criar novo post e validar schema")
def test_create_post_schema():
    payload = {"title": "foo", "body": "bar", "userId": 1}

    with allure.step("Enviar POST para /posts"):
        response = client.post("/posts", json=payload)
        assert response.status_code == 201

    with allure.step("Validar schema da resposta"):
        data = response.json()
        post = PostSchema(**data)
        assert post.title == payload["title"]
        assert post.body == payload["body"]
        assert post.userId == payload["userId"]
        assert isinstance(post.id, int)

# ----------------------------
# Teste extra: validação de tipos de dados
# ----------------------------
@allure.feature("API - Tipos de Dados")
def test_post_response_types():
    payload = {"title": "test", "body": "testing", "userId": 10}

    with allure.step("Enviar POST para /posts"):
        response = client.post("/posts", json=payload)
        assert response.status_code == 201

    with allure.step("Validar tipos de dados da resposta"):
        data = response.json()
        assert isinstance(data["id"], int)
        assert isinstance(data["title"], str)
        assert isinstance(data["body"], str)
        assert isinstance(data["userId"], int)
