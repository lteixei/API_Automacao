# tests/test_api_advanced.py
import pytest
from utils.api_client import APIClient
from tests.schemas import PostSchema
import allure

# Instanciando o client antes de qualquer teste
client = APIClient("https://jsonplaceholder.typicode.com")

# =======================
# Testes GET parametrizados
# =======================
@pytest.mark.parametrize("endpoint, expected_count", [
    ("/posts", 100),
    ("/comments", 500),
    ("/albums", 100)
])
@allure.feature("GET Endpoints")
@allure.story("Validação de quantidade de recursos")
def test_get_endpoints(endpoint, expected_count):
    response = client.get(endpoint)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == expected_count

# =======================
# Testes POST com schema
# =======================
@allure.feature("Posts")
@allure.story("Criar novo post e validar schema")
def test_create_post_schema_allure():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = client.post("/posts", json=payload)
    assert response.status_code == 201

    # Validação de schema
    data = response.json()
    PostSchema(**data)

@allure.feature("Posts")
@allure.story("Criar novo post com validação de conteúdo")
def test_create_post_schema_basic():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = client.post("/posts", json=payload)
    assert response.status_code == 201

    # Validação de schema
    data = response.json()
    post = PostSchema(**data)
    assert post.title == payload["title"]
    assert post.body == payload["body"]
    assert post.userId == payload["userId"]
