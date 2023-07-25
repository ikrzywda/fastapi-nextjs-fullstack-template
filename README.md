# Template for fullstack application using FastAPI and NextJS

## Features

- **Python** backend with **FastAPI**
  - **SQLModel** as ORM
- **Alembic** migrations with SQLModel
- **Basic Postgres Docker** setup
- **NextJS** frontend
  - using **Redux** for state managament
  - **RTK Query client generation** based on OpenAPI spec

## Currently working on

- **Backend**

  - [ ] Writing tests
  - [ ] Improved setup for migrations

- **Frontend**

  - [ ] Todo Demo application
  - [ ] Admin Panel

- **CI/CD**
  - [ ] Running tests on CI server (GH Actions)

## How to run

### Backend

> setup python environment

```bash
pip install poetry
cd backend/app
poetry install
```

> start backend

```bash
cd backend/app
cp .env.sample .env
docker compose up   # first terminal
./start-api.sh  # second terminal
```

### Frontend

```bash
cd frontend
pnpm
pnpm dev
```

## Acknowlegments

- template is heavily based on [Tiangolo's fullstack template](https://github.com/tiangolo/full-stack-fastapi-postgresql)
