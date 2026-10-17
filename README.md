⚡ FastAPI Practice - Learning
<p align="center"> <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
 <img src="https://img.shields.io/badge/FastAPI-Learning-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
 <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
 <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge" alt="SQLAlchemy">
 <img src="https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest"> </p> <p align="center">   A hands-on project for learning FastAPI concepts, request handling, dependencies, middleware, database integration, and automated API testing.
</p>

📌 About the Project
FASTAPI PRACTICE - LEARNING is a practical Python project for understanding how FastAPI applications receive requests, process inputs, execute endpoint logic, and return responses.
The project follows a step-by-step learning approach, combining theory with implementation and testing. The focus is on understanding the request-to-response flow rather than only writing endpoint code.
🎯 Learning Objectives
- Understand FastAPI application structure and endpoint execution.
- Work with HTTP methods and CRUD operations.
- Use path parameters and query parameters.
- Understand request validation and response handling.
- Reuse logic with FastAPI dependencies and Depends().
- Understand middleware and request timing/logging.
- Explore PostgreSQL and SQLAlchemy concepts.
- Write automated API tests using pytest and FastAPI TestClient.
- Test endpoints through Swagger UI and, where useful, Postman.
- Understand how the components work together end to end.
🧩 Concepts Practiced
Topic	What it covers
FastAPI fundamentals	Application instance, routes, HTTP methods, and request-response flow
Path parameters	Values included in the URL path, often used to identify a resource
Query parameters	URL parameters used to filter or control returned results
Dependencies	Reusable logic and values supplied through Depends()
Middleware	Request-response processing, including timing and logging
Database concepts	PostgreSQL, SQLAlchemy, models, engines, and sessions
Automated testing	Test requests, status codes, and response assertions using pytest and TestClient


Scope note: Database setup and model exploration do not by themselves mean that all CRUD endpoints use persistent storage. Describe database CRUD as implemented only when the endpoints actually read and write records through PostgreSQL.

🔄 Request-to-Response Flow
A typical request follows this process:
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
Middleware can run around the request-response process to perform tasks such as measuring duration or logging the response status.
🛠️ Technology Stack
Backend
- Python — Main programming language.
- FastAPI — Framework for building APIs.
- Uvicorn — ASGI server for running the application.
- Pydantic — Data validation and structured request/response data, where configured.
Database Learning
- PostgreSQL — Relational database explored for persistent storage.
- SQLAlchemy — SQL toolkit and ORM explored for database interaction.
Testing and Tools
- pytest — Automated test runner.
- FastAPI TestClient — Sends test requests to the application.
- Swagger UI / OpenAPI — Interactive API documentation and schema.
- Postman — Manual API request testing.
- VS Code, Git, and GitHub — Development and version control.
⚙️ Setup and Installation
1. Clone the Repository
Replace the placeholder with your actual repository URL.
git clone <your-repository-url>
cd "FASTAPI PRACTICE - LEARNING"
2. Create a Virtual Environment
python -m venv .venv
Activate it on Windows PowerShell:
.venv\Scripts\Activate.ps1
3. Install Dependencies
If the project contains a requirements.txt file:
pip install -r requirements.txt
If dependencies are not yet recorded, install the packages required by the current project and then save them to requirements.txt.
4. Run the Application
If the application file is main.py and the FastAPI instance is named app:
uvicorn main:app --reload
5. Open API Documentation
Visit the following URL while the local server is running:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- OpenAPI schema: http://127.0.0.1:8000/openapi.json
Use the actual module name and application variable if they differ from these examples.
🧪 Automated Testing
The project uses pytest and FastAPI's TestClient to test API behavior without manually sending every request through a browser or Postman.
Run the test suite from the project root:
pytest
Tests can check:
- Expected HTTP status codes.
- Response JSON and returned values.
- Successful endpoint behavior.
- Missing or invalid input.
- Error responses for relevant cases.
Always rerun the tests before recording the current pass count in this README.
📚 Project Documentation
The docs/ directory contains focused notes for revision.
Document	Description
[01 - Project Overview](docs/01-overview.md)	Project purpose, components, and request-to-response flow
[02 - Path and Query Parameters](docs/02-path-query.md)	Parameter definitions, examples, and testing
[03 - Dependencies and Middleware](docs/03-dependencies.md)	Depends(), reusable logic, middleware, and execution flow
[04 - Database Integration](docs/04-database.md)	PostgreSQL, SQLAlchemy, models, sessions, and database flow
[05 - Automated Testing](docs/05-testing.md)	pytest, TestClient, assertions, and running tests


Recommended Learning Order
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
Filename note: Keep the database document named 04-database.md so the five documents have a unique, sequential numbering. If your current file is named 03-database.md, rename it to 04-database.md and keep 03-dependencies.md for dependencies and middleware.
🔐 Security and Git Hygiene
- Never commit .env files, database passwords, API keys, or other secrets.
- Add .venv/, venv/, __pycache__/, and .pytest_cache/ to .gitignore.
- Use environment variables for sensitive configuration.
- Avoid using production credentials or production data in tests.
⚠️ Current Scope and Limitations
This repository is a learning project. Its implemented behavior depends on the current source code.
- Path and query parameter handling has been studied and practiced.
- Dependencies and middleware have been explored for reusable logic and request processing.
- PostgreSQL and SQLAlchemy concepts have been explored; verify the endpoint code before claiming that all CRUD operations are database-backed.
- Automated tests should be rerun to confirm their current status.
- Production deployment, authentication, and other advanced features should only be listed as implemented when they are actually present in the repository.
🎓 Learning Outcomes
This project is intended to build a practical understanding of:
- How FastAPI routes and processes HTTP requests.
- How path and query parameters provide input to endpoints.
- How dependencies share logic and provide resources.
- How middleware wraps request-response processing.
- How SQLAlchemy components relate to PostgreSQL integration.
- How automated tests validate API behavior.
- How to trace the flow from an incoming request to the final response.
⭐ Final Takeaway
The main goal of FASTAPI PRACTICE - LEARNING is to understand how FastAPI components work together. The project progresses from request handling and parameters to reusable dependencies, middleware, database concepts, and automated testing.
Key takeaway: Learn not only how to create an endpoint, but also how its inputs are validated, how its logic runs, how data is accessed, and how the response is tested.
