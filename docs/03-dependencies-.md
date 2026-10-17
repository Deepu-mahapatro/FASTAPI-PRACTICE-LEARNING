03. Dependencies and Middleware
1. What Are Dependencies?
Dependencies are reusable functions or components that FastAPI executes when an endpoint needs them. They are declared using Depends().
2. Why Use Dependencies?
Dependencies reduce repeated code and help share common logic across endpoints. They can provide query parameters, validate requirements, or supply resources such as database sessions.
3. Basic Dependency Example
from fastapi import Depends, FastAPI

app = FastAPI()

def common_parameters(limit: int = 10):
    return {"limit": limit}

@app.get("/products")
def get_products(params: dict = Depends(common_parameters)):
    return params
Example request:
GET /products?limit=5
Example response:
{
  "limit": 5
}
In this example, FastAPI calls common_parameters() and passes its return value to the endpoint as params.
4. Dependency Execution Flow
1. The client sends a request.
2. FastAPI matches the route.
3. FastAPI identifies the declared dependency.
4. FastAPI executes the dependency function.
5. The dependency result is passed to the endpoint.
6. The endpoint executes and returns a response.
5. What Is Middleware?
Middleware is code that runs around the HTTP request-response process. It can perform work before the request reaches the endpoint and after the endpoint produces a response.
Common uses include request logging, measuring request duration, adding headers, and recording response status codes.
6. Middleware Example
import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_request(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    duration = time.perf_counter() - start_time

    print(
        f"{request.method} {request.url.path} "
        f"- {response.status_code} - {duration:.4f}s"
    )
    return response
call_next(request) passes the request through the remaining application and returns the resulting response. The middleware logs the method, path, status code, and elapsed time.
7. Middleware Execution Flow
1. The client sends an HTTP request.
2. Middleware performs its pre-request work.
3. The request continues through the application to the endpoint.
4. The endpoint produces a response.
5. Middleware performs its post-response work.
6. The response returns to the client.
8. Dependencies vs Middleware
Feature	Dependencies	Middleware
Main purpose	Reuse logic required by endpoints	Handle cross-cutting request-response tasks
Execution	When required by an endpoint	For requests passing through the middleware
Typical use	Shared parameters or database session	Request timing and logging
Endpoint values	Can pass returned values into endpoint parameters	Works with the request and response


9. How to Test
Dependencies
1. Start the application.
2. Open /docs on your local server.
3. Execute an endpoint that uses the dependency.
4. Try a query value such as limit=5.
5. Check the returned JSON.
Middleware
1. Send a request to an endpoint.
2. Check the terminal output.
3. Verify the method, path, response status, and duration are logged.
4. Confirm the response is returned correctly.
10. Key Takeaways
- Depends() declares reusable dependency logic.
- FastAPI executes the dependency and supplies its result to the endpoint.
- Middleware runs around the request-response process.
- call_next(request) passes the request onward and returns the response.
- Dependencies and middleware serve different purposes.
