## 🛠️ Automação de Testes de API

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
pip install -r requirements.txt  

2. Execute todos os testes:  
set PYTHONPATH=%CD% && pytest --alluredir=results  

---

## 🔹 Funcionalidades dos Testes

- Testes GET, POST, PUT e DELETE.  
- Validação completa de schemas usando Pydantic.  
- Testes parametrizados para múltiplos endpoints.  
- Relatórios profissionais com Allure, organizados por feature e story.  
- Fácil expansão para novas APIs e endpoints.  

---

## 🖼️ Exemplo de Relatório Allure

- Exemplo de relatório Allure com detalhes de testes, status e gráficos.

---

## 📦 Exemplo de Teste
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

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Abra uma Issue ou envie um Pull Request com melhorias, novos cenários ou exemplos de integração.

---

## 🤝 Boas práticas para contribuições: 

📌 Escreva código limpo, legível e documentado.  
📌 Teste suas mudanças antes de enviar o Pull Request.  
📌 Mantenha a consistência com o estilo e padrões do projeto.  
📌 Discuta melhorias ou dúvidas antes de implementar grandes mudanças.

---

## 👩‍💻 Contato

- Informações	
- Nome	Leonardo da Motta Teixeira  
- Cargo	QA Engineer / Gestor / Tester-Sênior  
- LinkedIn	www.linkedin.com/in/leonardo-da-motta-teixeira-3584734b  
- E-mail	lteixei@hotmail.com  

---

## 📝 Licença

- Este projeto está licenciado sob a MIT License.
