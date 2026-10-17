# 01. FastAPI Project Overview

## 1. What is FastAPI?

FastAPI is a Python web framework used to build APIs. It allows clients to communicate with backend applications through HTTP requests and responses.

## 2. Purpose of FastAPI

FastAPI helps developers create API endpoints for operations such as retrieving, creating, updating, and deleting data. It also supports input validation, automatic API documentation, and asynchronous programming.

## 3. Core Components

| Component | Purpose |
|---|---|
| Client | Sends HTTP requests to the API |
| Uvicorn | Runs the FastAPI application as an ASGI server |
| FastAPI | Matches routes and handles request processing |
| Endpoint | Executes the logic for a specific route |
| Response | Returns data and an HTTP status code to the client |

## 4. API Endpoint Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}
```

**Explanation:**

- `FastAPI()` creates the application instance.
- `@app.get("/")` defines a GET endpoint for the root path.
- `home()` executes when the matching request is received.
- The dictionary is returned as a JSON response.

## 5. End-to-End Request Flow

1. The client sends an HTTP request.
2. Uvicorn receives the incoming request.
3. FastAPI identifies the matching route.
4. FastAPI validates the declared inputs.
5. The endpoint function executes its logic.
6. FastAPI prepares the response.
7. Uvicorn sends the response back to the client.

## 6. HTTP Methods

| Method | Purpose |
|---|---|
| `GET` | Retrieve data |
| `POST` | Create data |
| `PUT` | Replace an existing resource |
| `PATCH` | Partially update a resource |
| `DELETE` | Delete a resource |

## 7. Request Validation

FastAPI validates parameters and request-body data according to the declared types and models. If the input is invalid, FastAPI normally returns a validation error instead of executing the endpoint with invalid data.

## 8. Response and Status Codes

An API response contains a status code and response data.

Common examples:

- `200 OK` — Request completed successfully.
- `201 Created` — Resource created successfully.
- `404 Not Found` — Requested resource was not found.
- `422 Unprocessable Entity` — Request data failed validation.

## 9. Run the Application

If the application is in `main.py` and the FastAPI instance is named `app`, run:

```bash
uvicorn main:app --reload
```

Open the following path on your local server:

- `/docs` — Interactive Swagger UI documentation.
- `/openapi.json` — Generated OpenAPI schema.

## 10. Key Takeaways

- FastAPI is used to build Python APIs.
- Uvicorn runs the application and handles the ASGI server layer.
- Routes connect HTTP requests to endpoint functions.
- Validation checks incoming data against declared requirements.
- The endpoint processes the request and returns a response.
- Swagger UI helps developers explore and test available endpoints.

**Next document:** `02-path-query.md` — Path Parameters and Query Parameters.
