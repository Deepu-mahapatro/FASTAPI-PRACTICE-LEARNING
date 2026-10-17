05. Automated Testing with pytest and FastAPI TestClient
1. What Is Automated Testing?
Automated testing uses code to check whether an application behaves as expected. It helps catch errors when code changes and reduces the need to repeat every test manually.
2. What Is pytest?
pytest is a Python testing framework. It discovers test functions and runs assertions to report whether they pass or fail.
3. What Is FastAPI TestClient?
FastAPI's TestClient lets tests send HTTP requests to the application without manually starting a server. It is commonly used with pytest.
4. Basic Test Example
This is a generic example. Adjust the route and expected response to match an endpoint in your project.
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
The test sends a GET request to / and checks that the response status code is 200.
5. What Should Tests Check?
Tests can verify:
- HTTP status codes.
- Response JSON and expected values.
- Successful requests.
- Invalid inputs and validation errors.
- Missing resources and error responses.
- Behavior for relevant edge cases.
6. Test Execution Flow
1. pytest discovers the test files and test functions.
2. The test creates or uses a TestClient.
3. The client sends a request to the FastAPI application.
4. The endpoint processes the request.
5. The test receives the response.
6. Assertions compare the actual result with the expected result.
7. pytest reports passed and failed tests.
7. Run the Tests
From the project root, with the project's virtual environment activated, run:
pytest
To show more detailed test names and results:
pytest -v
8. Understanding Test Results
- Passed: The test's assertions succeeded.
- Failed: An assertion did not match the expected result.
- Error: The test could not complete because of an unexpected problem, such as a setup or import error.
When a test fails, read the traceback, identify the failing assertion or setup step, fix the cause, and rerun the tests.
9. Good Testing Practices
- Use test cases that match the actual API behavior.
- Test both successful and unsuccessful requests.
- Keep tests independent where possible.
- Avoid using production credentials or production data.
- Configure a safe test database if tests perform database operations.
- Rerun tests after changing code.
- Report a test count only after confirming the current test output.
10. Key Takeaways
- pytest runs automated Python tests.
- TestClient sends requests to the FastAPI application during tests.
- Assertions check status codes and response data.
- Tests help detect regressions when code changes.
- A test example must use a route that actually exists in the project.
