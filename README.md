# 🧪 Desafio Técnico - Backend Python (FastAPI)


### Pré-requisitos

- Docker
- Docker Compose

---

### 🔧 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/currency-converter-app.git
cd currency-converter-app

```

### 🗝️ 2. Configure as variáveis de ambiente
Backend - backend/.env
```.env

DATABASE_URL=postgresql://postgres:postgres@db:5432/currency
CURRENCY_API_KEY=sua_api_key_aqui
ENV=dev
```

### 🐳 3. Rode o projeto com Docker Compose

```
docker-compose up --build
```
