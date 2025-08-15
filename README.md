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

arduino
Copiar
Editar

Se você quiser, posso criar **uma versão ainda mais profissional e visual**, com badges de PyPI, Python, Build, e Allure, que deixa o README parecido com repositórios grandes do GitHub.  

Quer que eu faça isso?







Você disse:
crie com imagens e mais profissional


O ChatGPT disse:
Perfeito! Vou criar uma versão profissional e visual do README, incluindo badges, imagens de exemplo de relatório Allure, e organização por seções, para que fique parecido com repositórios grandes do GitHub.

Aqui está:

markdown
Copiar
Editar
# 🛠️ Automação de Testes de API

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Pytest](https://img.shields.io/badge/Pytest-7.4.0-orange?logo=pytest)
![Allure](https://img.shields.io/badge/Allure-2.15.0-red)
![License](https://img.shields.io/badge/License-MIT-green)

> Estrutura completa de automação de testes de APIs REST, com validação de schemas, testes parametrizados e relatórios avançados.

---

## 📂 Estrutura do Projeto

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

## 🚀 Tecnologias Utilizadas

- **Python 3.13**
- **Pytest** - framework de testes
- **Requests** - para chamadas HTTP
- **Pydantic** - validação de schemas
- **Allure** - relatórios profissionais
- **Faker** - geração de dados falsos
- **Git** - controle de versão

---

## 🧪 Como Executar os Testes

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
🔹 Funcionalidades dos Testes
Testes GET, POST, PUT e DELETE.

Validação completa de schemas usando Pydantic.

Testes parametrizados para múltiplos endpoints.

Relatórios profissionais com Allure, organizados por feature e story.

Fácil expansão para novas APIs e endpoints.

🖼️ Exemplo de Relatório Allure

Exemplo de relatório Allure com detalhes de testes, status e gráficos.

📦 Exemplo de Teste
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
🤝 Contribuindo
Faça um fork do repositório.

Crie sua branch: git checkout -b minha-feature.

Faça suas alterações e commit: git commit -m "Descrição da alteração".

Envie para o repositório remoto: git push origin minha-feature.

Abra um Pull Request.

📄 Licença
Este projeto está licenciado sob a MIT License.
