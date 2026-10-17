# ⚡ FastAPI Practice - Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Learning-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest">
</p>

<p align="center">
  <strong>A hands-on project for learning FastAPI, request handling, dependencies, middleware, database integration, and automated API testing.</strong>
</p>

---

## 📌 About the Project

**FASTAPI PRACTICE - LEARNING** is a practical Python project focused on understanding how FastAPI applications receive requests, validate inputs, execute endpoint logic, interact with data, and return responses.

The project follows a step-by-step learning approach, combining theory, implementation, and testing. The main objective is to understand the complete request-to-response flow rather than simply writing endpoint code.

## 🎯 Learning Objectives

- Understand FastAPI application structure and endpoint execution.
- Practice HTTP methods and CRUD operations.
- Work with path parameters and query parameters.
- Understand request validation and response handling.
- Implement reusable logic using `Depends()`.
- Understand middleware and request timing/logging.
- Explore PostgreSQL and SQLAlchemy.
- Write automated tests using `pytest` and FastAPI `TestClient`.
- Test APIs using Swagger UI and Postman.
- Understand the end-to-end API execution flow.

---

## 🧩 Concepts Practiced

| Topic | Description |
|---|---|
| FastAPI Fundamentals | Application instance, routes, HTTP methods, and request-response flow |
| Path Parameters | Values included in the URL path to identify a resource |
| Query Parameters | URL parameters used to filter or control results |
| Dependencies | Reusable logic and values provided through `Depends()` |
| Middleware | Request-response processing, timing, and logging |
| Database Integration | PostgreSQL, SQLAlchemy, models, engines, and sessions |
| Automated Testing | Test requests, status codes, and response assertions using `pytest` and `TestClient` |

> **Scope note:** Database setup and model exploration do not automatically mean that all CRUD endpoints use persistent storage. Database-backed CRUD should be described as implemented only when the endpoints actually read and write records through PostgreSQL.

---

## 🔄 Request-to-Response Flow

A typical request follows this process:

```text
       Client / Swagger UI / Postman
                    |
                    v
                 Uvicorn
               ASGI Server
                    |
                    v
                 FastAPI
              Route Matching
                    |
                    v
        Input Validation and Dependencies
                    |
                    v
             Endpoint Function
                    |
                    v
           Application / Data Operations
                    |
                    v
            Response Processing
                    |
                    v
          JSON + HTTP Status Code
                    |
                    v
                  Client
```

Middleware can run around the request-response process to perform tasks such as measuring request duration or logging response status.

## 🛠️ Technology Stack

### Backend

- **Python** — Main programming language.
- **FastAPI** — Framework for building APIs.
- **Uvicorn** — ASGI server for running the application.
- **Pydantic** — Data validation and structured request/response data.

### Database

- **PostgreSQL** — Relational database explored for persistent storage.
- **SQLAlchemy** — SQL toolkit and ORM explored for database interaction.

### Testing and Development Tools

- **pytest** — Automated test runner.
- **FastAPI TestClient** — Sends test requests to the application.
- **Swagger UI / OpenAPI** — Interactive API documentation and schema.
- **Postman** — Manual API testing.
- **VS Code** — Code editor.
- **Git and GitHub** — Version control and source code hosting.

---

## ⚙️ Setup and Installation

### 1. Clone the Repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone <your-repository-url>
cd "FASTAPI PRACTICE - LEARNING"
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

If the application is in `main.py` and the FastAPI instance is named `app`:

```bash
uvicorn main:app --reload
```

Use the correct module name and application variable if your project differs.

### 5. Open API Documentation

With the local server running, visit:

| URL | Purpose |
|---|---|
| `http://127.0.0.1:8000/docs` | Swagger UI |
| `http://127.0.0.1:8000/redoc` | ReDoc documentation |
| `http://127.0.0.1:8000/openapi.json` | OpenAPI schema |

---

## 🧪 Automated Testing

The project uses `pytest` and FastAPI's `TestClient` to verify API behavior without manually sending every request through a browser or Postman.

Run tests from the project root:

```bash
pytest
```

For detailed output:

```bash
pytest -v
```

Tests can verify:

- Expected HTTP status codes.
- Response JSON and returned values.
- Successful endpoint behavior.
- Missing or invalid input.
- Error responses for relevant cases.

Always rerun the tests before reporting the current number of passed tests.

---

## 📚 Project Documentation

The `docs/` directory contains focused documentation for learning and revision.

| Document | Description |
|---|---|
| [01 - Project Overview](docs/01-overview.md) | Project purpose, components, and request-to-response flow |
| [02 - Path and Query Parameters](docs/02-path-query.md) | Parameter definitions, examples, and testing |
| [03 - Dependencies and Middleware](docs/03-dependencies.md) | `Depends()`, reusable logic, middleware, and execution flow |
| [04 - Database Integration](docs/04-database.md) | PostgreSQL, SQLAlchemy, models, sessions, and database flow |
| [05 - Automated Testing](docs/05-testing.md) | `pytest`, `TestClient`, assertions, and running tests |

### Recommended Learning Order

```text
01. Project Overview
        |
        v
02. Path and Query Parameters
        |
        v
03. Dependencies and Middleware
        |
        v
04. Database Integration
        |
        v
05. Automated Testing
```

**Important:** Ensure the filenames above match the actual files in your `docs/` folder. Use `03-dependencies.md` for dependencies and middleware, and `04-database.md` for database documentation.

---

## 🔐 Security and Git Hygiene

- Never commit `.env` files, database passwords, API keys, or other secrets.
- Add `.venv/`, `venv/`, `__pycache__/`, `*.py[cod]`, and `.pytest_cache/` to `.gitignore`.
- Store sensitive configuration in environment variables.
- Avoid using production credentials or production data in tests.
- Do not upload the virtual environment; recreate it using `requirements.txt`.

---

## ⚠️ Current Scope and Limitations

This repository is a learning project. Its actual features depend on the current source code.

- Path and query parameter handling has been studied and practiced.
- Dependencies and middleware have been explored for reusable logic and request processing.
- PostgreSQL and SQLAlchemy concepts have been explored; verify the endpoint code before claiming that all CRUD operations are database-backed.
- Automated tests should be rerun to confirm their current status.
- Deployment, authentication, and other advanced features should only be listed as implemented if they are actually present.

---

## 🎓 Learning Outcomes

This project develops practical understanding of:

- How FastAPI routes and processes HTTP requests.
- How path and query parameters provide input to endpoints.
- How dependencies share logic and provide resources.
- How middleware wraps request-response processing.
- How SQLAlchemy components relate to PostgreSQL integration.
- How automated tests validate API behavior.
- How to trace a request from the client to the final response.

---

## ⭐ Final Takeaway

**FASTAPI PRACTICE - LEARNING** builds a foundation in API development by progressing from request handling and parameters to dependencies, middleware, database concepts, and automated testing.

> **Key takeaway:** Understand not only how to create an endpoint, but also how its inputs are validated, how its logic runs, how data is accessed, and how the final response is tested.

---

<p align="center">
  Built as a step-by-step FastAPI learning project.
</p>
