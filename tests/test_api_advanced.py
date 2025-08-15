# tests/test_api_advanced.py
import pytest
from utils.api_client import APIClient

client = APIClient("https://jsonplaceholder.typicode.com")

# Teste GET para múltiplos recursos
@pytest.mark.parametrize("endpoint,status_code", [
    ("/posts", 200),
    ("/comments", 200),
    ("/albums", 200),
])
def test_get_endpoints(endpoint, status_code):
    response = client.get(endpoint)
    assert response.status_code == status_code
    assert response.json() is not None

# Teste POST
def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = client.post("/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

def test_post_response_schema():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = client.post("/posts", json=payload)
    data = response.json()

    # Validar tipos de dados
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)
    assert isinstance(data["userId"], int)