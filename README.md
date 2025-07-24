# Currency Converter Application

![App Screenshot](/screenshot.png)

A full-stack currency conversion application with transaction history tracking.

## Purpose

This application allows users to:
- Convert between 4 major currencies (BRL, USD, EUR, JPY)
- View their conversion history
- Get real-time exchange rates from CurrencyAPI

## Tech Stack

### Backend
- **Python 3.10+**
- **FastAPI** (REST API framework)
- **SQLAlchemy** (ORM)
- **AsyncPG** (PostgreSQL driver)
- **Pytest** (testing)
- **Poetry** (dependency management)

### Frontend
- **React 18** (TypeScript)
- **Material-UI** (UI components)
- **TailwindCSS** (utility CSS)
- **React Router** (navigation)
- **Axios** (HTTP client)
- **Vite** (build tool)

## Architectural Decisions

### Backend Architecture

#### Clean Architecture Approach

```
backend/
├── api/ # Interface layer
│ └── v1/ # API versioning
│ ├── endpoints/
│ └── routers.py
├── core/ # Configuration
├── db/ # Data layer
│ ├── models.py
│ ├── repositories.py
│ └── session.py
├── services/ # Business logic
└── schemas/ # Data validation
```

Key decisions:
1. **Async PostgreSQL**: Chose asyncpg over psycopg2 for better performance with FastAPI
2. **Layer Separation**: Strict separation between routes, services and repositories
3. **Alembic Migrations**: Database version control instead of metadata.create_all()
4. **CurrencyAPI Integration**: External rates provider with proper error handling

### Frontend Architecture

#### Component-Based Structure

```
frontend/
├── src/
│ ├── components/ # Reusable UI components
│ ├── pages/ # Route-level components
│ ├── services/ # API clients
│ ├── types/ # Type definitions
│ ├── App.tsx # Root component
│ └── main.tsx # Entry point
```

Key decisions:
1. **Atomic Design**: Components organized by complexity
2. **Centralized API Client**: Single Axios instance with interceptors
3. **TypeScript**: Strict typing throughout the application
4. **Tailwind + MUI**: Combined styling approach for rapid development

## Layer Organization

### Backend Layers

| Layer          | Responsibility                          | Example Files              |
|----------------|----------------------------------------|----------------------------|
| **API**        | HTTP interface, routing                | `endpoints/conversion.py`  |
| **Services**   | Business logic, use cases              | `services/conversion.py`   |
| **Repositories** | Database operations                   | `repositories.py`          |
| **Models**     | Data structure, ORM mapping           | `models.py`                |
| **Schemas**    | Request/response validation           | `schemas/conversion.py`    |

### Frontend Layers

| Layer          | Responsibility                          | Example Files              |
|----------------|----------------------------------------|----------------------------|
| **Components** | Presentational UI elements             | `CurrencyConverter.tsx`    |
| **Pages**      | Route-level components                 | `HomePage.tsx`             |
| **Services**   | API communication                      | `api.ts`                   |
| **Types**      | Type definitions                       | `conversion.ts`            |

## Getting Started

### Build and start services
```bash
docker compose up -d
```

### Monitor services startup
```bash
docker compose logs -f
```

### Initate database
```bash
docker compose exec backend poetry run alembic upgrade head
```


## Key Features

- Real-time currency conversion
- Transaction history tracking
- Responsive UI
- Comprehensive error handling
- Swagger API documentation
- Unit and integration tests
