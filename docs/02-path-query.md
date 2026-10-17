# 02. Path Parameters and Query Parameters

## 1. What are Path Parameters?

Path parameters are variables included directly in the URL path. They are commonly used to identify a specific resource.

**Example:**

```python
@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id}
```

**Request:**

```http
GET /products/5
```

Here, `5` is the path parameter value passed to `product_id`.

## 2. Purpose of Path Parameters

Path parameters help identify a specific resource, such as a product, user, or order.

Examples:
- `/products/5` — Identify product 5.
- `/users/10` — Identify user 10.
- `/orders/25` — Identify order 25.

## 3. What are Query Parameters?

Query parameters are values passed in the URL after a question mark (`?`). They are commonly used for filtering, searching, sorting, and controlling results.

**Example:**

```python
@app.get("/products")
def get_products(category: str | None = None, limit: int = 10):
    return {
        "category": category,
        "limit": limit
    }
```

**Request:**

```http
GET /products?category=electronics&limit=5
```

Here, `category` and `limit` are query parameters.

## 4. Purpose of Query Parameters

Query parameters allow clients to control which data the API returns without changing the endpoint path.

Examples:
- `/products?category=electronics` — Filter by category.
- `/products?limit=5` — Request a limit of five results.
- `/products?search=laptop` — Search using a term, if the endpoint implements that behavior.

## 5. Path vs Query Parameters

| Feature | Path Parameter | Query Parameter |
|---|---|---|
| Location | Inside the URL path | After `?` |
| Main purpose | Identify a resource | Filter or control results |
| Example | `/products/5` | `/products?limit=5` |
| Required? | Normally required for that route | Can be optional or required |

## 6. Required and Optional Parameters

FastAPI determines parameter requirements from the route and function declaration.

```python
@app.get("/products/{product_id}")
def get_product(product_id: int, limit: int = 10):
    return {"product_id": product_id, "limit": limit}
```

- `product_id` is required because it is part of the route.
- `limit` is optional because it has a default value of `10`.
- If `limit` is omitted, FastAPI uses the default value.

## 7. Type Validation

FastAPI validates declared parameter types.

For example, if `product_id` is declared as an integer, sending a non-integer value such as `/products/abc` normally produces a validation error.

Type declarations make APIs easier to understand and help reject invalid input.

## 8. How to Test in Swagger UI

1. Start the FastAPI application.
2. Open `/docs` on your local server.
3. Select the endpoint you want to test.
4. Click **Try it out**.
5. Enter the path or query parameter values.
6. Click **Execute**.
7. Review the request URL, response body, and status code.

## 9. How to Test in Postman

For a path parameter:

```http
GET http://127.0.0.1:8000/products/5
```

For query parameters:

```http
GET http://127.0.0.1:8000/products?category=electronics&limit=5
```

Replace the examples with the actual host and routes used by your project. Check both valid and invalid inputs.

## 10. Key Takeaways

- Path parameters are commonly used to identify a particular resource.
- Query parameters are commonly used to filter or control returned data.
- Path parameters appear inside the URL path.
- Query parameters appear after `?` and multiple values are separated by `&`.
- FastAPI validates parameters based on their declared types and requirements.
- Swagger UI and Postman help test endpoint behavior.

