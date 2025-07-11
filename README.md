# 🧪 Desafio Técnico - Backend Python (FastAPI)

## 💸 Conversor de Moedas

Você deverá implementar uma aplicação que permita a conversão de valores entre moedas, utilizando **Python com FastAPI** no backend. O frontend pode ser opcionalmente implementado em Vue.js ou React.

> **Importante:** Caso você não tenha experiência com frontend, a entrega pode ser feita exclusivamente com a API.

---

## 📆 Requisitos do Projeto

### ✅ Funcionalidades Principais
- A API deve permitir a conversão entre pelo menos 4 moedas:
  - BRL (Real)
  - USD (Dólar Americano)
  - EUR (Euro)
  - JPY (Iene)

- As taxas de câmbio devem ser obtidas da API:
  - https://app.currencyapi.com/
  - Documentação: https://currencyapi.com/docs

### 🔐 Persistência das Transações
Cada transação realizada deve ser registrada com as seguintes informações:
- ID do usuário
- Moeda de origem e destino
- Valor de origem
- Valor convertido
- Taxa de conversão
- Data/Hora UTC

### 🔍 Endpoint de Consulta
- `GET /transactions?userId=123`

#### Exemplo de retorno:
```json
{
  "transactionId": 42,
  "userId": 123,
  "fromCurrency": "USD",
  "toCurrency": "BRL",
  "fromValue": 100,
  "toValue": 525.32,
  "rate": 5.2532,
  "timestamp": "2024-05-19T18:00:00Z"
}
```

### ❌ Casos de Erro
Deverão retornar:
- Código HTTP apropriado
- Mensagem de erro clara e objetiva

---

## 🧪 Testes
- A aplicação deve conter testes unitários e de integração com `pytest`

---

## 📄 README.md
Deve conter:
- Instruções para executar o projeto
- Explicação do propósito
- Principais decisões de arquitetura
- Organização das camadas (ex: routers, services, repositories, models)
- O conteúdo deve estar todo em inglês

---

## 🧰 Itens Desejáveis (Diferenciais)
- Logs estruturados (ex: `loguru`, `structlog`)
- Tratamento de exceções com middlewares
- Documentação automática (Swagger já embutido no FastAPI)
- Linter (ex: `ruff`, `black`, `flake8`)
- Deploy funcional (ex: Render, Railway, Fly.io)
- CI/CD com GitHub Actions

### Frontend (opcional)
- Vue.js 3 + TypeScript ou React + TypeScript
- TailwindCSS
- Axios
- Testes com Cypress, RTL ou Vitest

---

## 🚀 Tecnologias Esperadas

### Backend
- Python 3.10+
- FastAPI
- SQLAlchemy 2.x ou Tortoise ORM
- PostgreSQL ou SQLite
- Pytest

---

## ⭐ Perfil Desejado
- Boas práticas REST
- Arquitetura limpa e escalável
- Conhecimentos em AWS são diferenciais
- Experiência com CI/CD
- Boa comunicação e clareza de código

---

## 📋 Entrega
1. Crie um repositório público no GitHub
2. Crie uma branch com seu nome em snake_case (ex: `joao_silva_souza`)
3. Suba seu código com commits organizados
4. Abra um Pull Request com:
   - **Título:** `Entrega - joao_silva_souza`
   - **Descrição:** Nome completo, data da entrega e observações

---

## 📢 Considerações Finais
- Cite alternativas gratuitas caso use serviços pagos
- Clareza, boas práticas e organização serão avaliadas
- Pode adicionar um `THOUGHTS.md` com decisões técnicas e observações

Boa sorte! 🚀
