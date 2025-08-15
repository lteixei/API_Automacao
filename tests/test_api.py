import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users_status_code():
    """
    Verifica se a requisição GET /users retorna status 200
    """
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

def test_get_user_by_id():
    """
    Verifica se é possível buscar um usuário pelo ID e validar seu nome
    """
    user_id = 1
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    data = response.json()
    
    assert response.status_code == 200
    assert data["id"] == user_id
    assert "Leanne Graham" in data["name"]
