# 05. Automated Testing in FastAPI

## 1. What is Automated Testing?

Automated testing is the process of using code to check whether an application behaves as expected.

In FastAPI, automated tests can send requests to endpoints, check response data, and verify HTTP status codes without manually testing every request in Swagger UI or Postman.

**Example:**

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}
```

A test can automatically send a request to `/` and verify the returned response.

## 2. Purpose of Automated Testing

Automated testing helps developers verify that an API works correctly.

Common purposes:
- Check whether endpoints return the expected responses.
- Verify HTTP status codes.
- Test valid and invalid inputs.
- Detect errors when code changes.
- Check that existing functionality continues to work.
- Reduce repetitive manual testing.

## 3. What is pytest?

`pytest` is a Python testing framework used to write and execute automated tests.

It discovers test files, runs test functions, and reports which tests passed or failed.

**Example test file: `test_main.py`**

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to FastAPI"
    }
```

Here:
- `TestClient` sends a test request to the FastAPI application.
- `client.get("/")` sends a GET request to the root endpoint.
- `response.status_code` contains the HTTP status code.
- `response.json()` returns the response body as Python data.
- `assert` checks whether the actual result matches the expected result.

## 4. What is FastAPI TestClient?

`TestClient` is a testing utility provided by FastAPI through Starlette. It allows tests to send HTTP-style requests directly to the application without starting a separate Uvicorn server.

**Example:**

```python
response = client.get("/")
```

This sends a GET request to the root endpoint.

Other commonly used methods include:

```python
client.get("/")
client.post("/products", json={"name": "Laptop"})
client.put("/products/1", json={"name": "Updated Laptop"})
client.patch("/products/1", json={"name": "New Laptop"})
client.delete("/products/1")
```

Use the methods and request data that match the endpoints actually implemented in your application.

## 5. Understanding Assertions

Assertions verify whether the application's behavior matches expectations.

**Example:**

```python
assert response.status_code == 200
assert response.json()["message"] == "Welcome to FastAPI"
```

Here:
- The first assertion checks the HTTP status code.
- The second assertion checks the value of the `message` field.
- If an assertion fails, pytest reports the test as failed.

Common HTTP status codes to test include:

| Status Code | Meaning |
|---|---|
| `200 OK` | Request succeeded |
| `201 Created` | Resource created successfully |
| `204 No Content` | Request succeeded without a response body |
| `400 Bad Request` | Request cannot be processed because of a client error |
| `404 Not Found` | Requested resource was not found |
| `422 Unprocessable Entity` | Request validation failed in FastAPI's usual validation behavior |
| `500 Internal Server Error` | Unexpected server-side error |

Test the status codes appropriate to each endpoint's behavior.

## 6. How to Run Automated Tests

Run commands from the project root, where your `test_main.py` file is located.

### Run All Tests

```bash
pytest
```

This discovers and runs the tests that pytest recognizes.

### Run Tests with Detailed Output

```bash
pytest -v
```

The `-v` option displays individual test names and their results.

### Run a Specific Test File

```bash
pytest test_main.py
```

### Run a Specific Test Function

```bash
pytest test_main.py::test_home
```

## 7. Understanding Test Results

A successful test may display output similar to:

```text
test_main.py::test_home PASSED
```

A failed test may display:

```text
test_main.py::test_home FAILED
```

When a test fails, inspect the error details to identify whether the issue is in the endpoint, the expected result, the test setup, or an external dependency.

Do not record a specific number of passed tests in the project documentation without running the current test suite.

## 8. How to Test in Swagger UI

Swagger UI is useful for manually exploring and testing API endpoints.

1. Start the application.
2. Open `http://127.0.0.1:8000/docs`.
3. Select an endpoint.
4. Click **Try it out**.
5. Enter the required parameters or request body.
6. Click **Execute**.
7. Review the response body and HTTP status code.

Swagger UI is mainly for interactive manual testing, while pytest automates repeatable checks.

## 9. Automated Testing vs Manual Testing

| Feature | Automated Testing | Manual Testing |
|---|---|---|
| Method | Tests are executed by code | Requests are sent and inspected manually |
| Tools | pytest, TestClient | Swagger UI, Postman |
| Repetition | Easy to repeat | Requires repeating the steps |
| Best use | Regression checks and repeatable verification | Exploring endpoints and inspecting responses |
| Results | Pass/fail reports and assertion details | Results inspected by the developer |

Both approaches are useful during API development.

## 10. End-to-End Testing Flow

```text
Developer Writes a Test
          |
          v
       Runs pytest
          |
          v
   TestClient Sends Request
          |
          v
   FastAPI Processes Request
          |
          v
   Endpoint Returns Response
          |
          v
 Test Receives Response
          |
          v
 Assertions Check the Result
          |
          v
    Test Passes or Fails
```

This flow helps verify the behavior of an endpoint automatically.

## 11. Key Takeaways

- Automated testing verifies application behavior using code.
- `pytest` discovers and runs Python tests.
- `TestClient` sends requests directly to a FastAPI application without a separate Uvicorn server.
- Assertions check status codes and response data.
- Swagger UI and Postman are useful for manual API testing.
- Run tests after code changes to check whether existing behavior still works.
- A passing test confirms the behavior checked by that test, not that the entire application is error-free.
