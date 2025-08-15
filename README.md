# Automação de Testes de API

Este projeto contém uma **estrutura completa de automação de testes para APIs** utilizando Python, Pytest e Pydantic, com integração de relatórios Allure.

---

## Tecnologias Utilizadas

- **Python 3.13**
- **Pytest** - framework de testes
- **Requests** - para chamadas HTTP
- **Pydantic** - validação de schemas
- **Allure** - relatórios avançados
- **Faker** - geração de dados falsos
- **Git** - controle de versão

---

## Estrutura do Projeto

API/
│
├─ tests/
│ ├─ test_api.py # Testes básicos de endpoints
│ ├─ test_api_advanced.py # Testes avançados com validação de schemas
│ ├─ test_api_master.py # Testes profissionais integrando múltiplos endpoints
│ └─ test_api_profissional.py # Testes completos com parametrização e Allure
│
├─ utils/
│ └─ api_client.py # Cliente API reutilizável
│
├─ schemas/
│ └─ PostSchema.py # Schemas Pydantic para validação
│
└─ README.md

yaml
Copiar
Editar

---

## Executando os Testes

1. Instale as dependências:

```bash
pip install -r requirements.txt
Execute todos os testes:

bash
Copiar
Editar
pytest
Execute com relatórios Allure:

bash
Copiar
Editar
pytest --alluredir=results
allure serve results
Funcionalidades dos Testes
Testes GET, POST, PUT e DELETE.

Validação completa de schemas usando Pydantic.

Testes parametrizados para múltiplos endpoints.

Relatórios profissionais com Allure, com organização por feature e story.

Possibilidade de expansão para testes de APIs internas ou externas.

Exemplo de Teste
python
Copiar
Editar
@pytest.mark.parametrize("endpoint, expected_count", [
    ("/posts", 100),
    ("/comments", 500),
    ("/albums", 100)
])
def test_get_endpoints(endpoint, expected_count):
    response = client.get(endpoint)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == expected_count
Contribuindo
Faça um fork do repositório.

Crie sua branch: git checkout -b minha-feature.

Faça suas alterações e commit: git commit -m "Descrição da alteração".

Envie para o repositório remoto: git push origin minha-feature.

Abra um Pull Request.

Licença
Este projeto está licenciado sob a MIT License.
