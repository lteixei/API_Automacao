# tests/test_api_full.py
import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"  # API de teste pública

# -----------------------------
# Fixtures
# -----------------------------
@pytest.fixture(scope="module")
def get_users():
    response = requests.get(f"{BASE_URL}/users")
    return response

@pytest.fixture
def new_post_payload():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

# -----------------------------
# Testes GET
# -----------------------------
def test_get_users_status(get_users):
    assert get_users.status_code == 200, "Status code deve ser 200"

def test_get_users_content(get_users):
    data = get_users.json()
    assert isinstance(data, list), "Resposta deve ser uma lista"
    assert len(data) > 0, "Lista de usuários não pode ser vazia"
    for user in data:
        assert "id" in user and "name" in user, "Usuário deve ter 'id' e 'name'"

# -----------------------------
# Testes POST
# -----------------------------
def test_create_post_status(new_post_payload):
    response = requests.post(f"{BASE_URL}/posts", json=new_post_payload)
    assert response.status_code == 201, "Status code deve ser 201"
    data = response.json()
    assert data["title"] == new_post_payload["title"]
    assert data["body"] == new_post_payload["body"]
    assert data["userId"] == new_post_payload["userId"]

def test_create_post_invalid():
    payload = {"invalid_field": "teste"}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    # JSONPlaceholder ignora campos inválidos, então verificamos se falta campo 'title'
    data = response.json()
    assert "title" not in data
