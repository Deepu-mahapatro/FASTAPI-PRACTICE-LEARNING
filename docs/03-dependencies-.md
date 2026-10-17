# 03. Dependencies and Middleware

## 1. What are Dependencies?

Dependencies are functions or callables that FastAPI executes when an endpoint needs reusable logic or a value.

FastAPI uses `Depends()` to declare that an endpoint depends on another function.

**Example:**

```python
from fastapi import FastAPI, Depends

app = FastAPI()


def get_message():
    return "Hello from dependency"


@app.get("/message")
def read_message(message: str = Depends(get_message)):
    return {"message": message}
```

**Request:**

```http
GET /message
```

**Response:**

```json
{
    "message": "Hello from dependency"
}
```

Here, FastAPI executes `get_message()` and passes its returned value to the `message` parameter.

## 2. Purpose of Dependencies

Dependencies help reuse common logic instead of repeating the same code in multiple endpoints.

Common use cases:
- Providing database sessions.
- Validating common parameters.
- Checking user permissions.
- Reusing shared application logic.
- Providing configuration values.

For example, multiple endpoints can use the same dependency to obtain a database session.

## 3. What is `Depends()`?

`Depends()` is a FastAPI function used to declare a dependency.

**Example:**

```python
def get_limit():
    return 10


@app.get("/products")
def get_products(limit: int = Depends(get_limit)):
    return {"limit": limit}
```

**Request:**

```http
GET /products
```

**Response:**

```json
{
    "limit": 10
}
```

Here:
- `get_limit()` is the dependency function.
- `Depends(get_limit)` tells FastAPI to execute the dependency.
- The returned value `10` is passed to the endpoint.
- The endpoint uses the value to create the response.

## 4. Dependency Execution Flow

When a client sends a request to an endpoint that uses a dependency, the flow is:

```text
Client Request
      |
      v
FastAPI Matches the Route
      |
      v
Executes Dependency Function
      |
      v
Gets the Returned Value
      |
      v
Passes Value to Endpoint
      |
      v
Endpoint Executes
      |
      v
Response Returned to Client
```

FastAPI resolves the required dependencies before executing the endpoint function.

## 5. What is Middleware?

Middleware is code that runs around the HTTP request-response process.

It can process a request before the endpoint executes and process the response before it is returned to the client.

**Example:**

```python
from fastapi import FastAPI, Request
import time

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    print(f"Request: {request.method} {request.url.path}")

    response = await call_next(request)

    duration = time.time() - start_time

    print(f"Status Code: {response.status_code}")
    print(f"Duration: {duration:.4f} seconds")

    return response


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}
```

Here, the middleware logs the incoming request, measures how long application processing takes, and records the response status code.

## 6. Purpose of Middleware

Middleware is useful for handling common behavior across requests.

Examples:
- Logging incoming requests.
- Measuring request-processing time.
- Recording response status codes.
- Adding or modifying response headers.
- Implementing other shared request-response processing.

Middleware is generally applied across the application, while dependencies can be configured for particular endpoints or routers.

## 7. Middleware Execution Flow

```text
Client Sends Request
        |
        v
Middleware Starts
        |
        v
Logs Request and Start Time
        |
        v
Request Continues Through Application
        |
        v
Endpoint Executes
        |
        v
Response Is Created
        |
        v
Middleware Processes Response
        |
        v
Logs Status and Duration
        |
        v
Response Returns to Client
```

The middleware executes code before and after `call_next(request)`. The code after that call runs when the downstream application returns a response.

## 8. Dependencies vs Middleware

| Feature | Dependencies | Middleware |
|---|---|---|
| Main purpose | Reuse logic and provide values | Process requests and responses |
| Scope | Applied where configured | Generally applies across the application |
| Endpoint values | Can provide values directly to endpoints | Works with the request-response cycle |
| Common examples | Database sessions, validation | Logging, timing, headers |
| Declaration | `Depends()` | `@app.middleware("http")` |

**Main difference:** Dependencies provide reusable logic or values to endpoints. Middleware wraps the request-response process.

## 9. How to Test in Swagger UI

1. Start the FastAPI application.
2. Open `/docs` on your local server.
3. Select the endpoint you want to test.
4. Click **Try it out**.
5. Click **Execute**.
6. Review the response body and status code.
7. For middleware, check the terminal output for request details and timing information.

For the dependency example, test:

```http
GET http://127.0.0.1:8000/message
```

For the middleware example, test:

```http
GET http://127.0.0.1:8000/
```

Use the actual routes configured in your application.

**Note:** These examples are independent. If you add them to the same `main.py`, keep a single `app = FastAPI()` declaration and combine the routes and middleware.

## 10. How to Test in Postman

For the dependency example:

```http
GET http://127.0.0.1:8000/message
```

Expected response:

```json
{
    "message": "Hello from dependency"
}
```

For the middleware example:

```http
GET http://127.0.0.1:8000/
```

Expected response:

```json
{
    "message": "Welcome to FastAPI"
}
```

Check the terminal to see the request method, URL path, status code, and processing duration printed by the middleware.

## 11. Key Takeaways

- Dependencies allow reusable logic and values to be shared through `Depends()`.
- Middleware processes requests and responses around the endpoint execution.
- Dependencies are useful for database sessions, validation, and shared application logic.
- Middleware is useful for logging, timing, and response processing.
- Swagger UI and Postman help test endpoint behavior.
- Both features help organize FastAPI applications and reduce duplicated code.
