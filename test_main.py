
# ============================================================
# FASTAPI AUTOMATED TESTING
# Project: FASTAPI PRACTICE LEARNING
# Tool: pytest + FastAPI TestClient
# ============================================================

import pytest
import main

from fastapi.testclient import TestClient


# ============================================================
# 1. TEST SETUP
# ============================================================

# Connect TestClient to the actual FastAPI application
client = TestClient(main.app)


# Reset the in-memory product data before every test.
# This prevents PUT, PATCH and DELETE tests from affecting
# the results of other tests.
@pytest.fixture(autouse=True)
def reset_products(monkeypatch):
    original_products = [
        {"id": 1, "name": "Laptop", "price": 50000},
        {"id": 2, "name": "Mouse", "price": 1000},
        {"id": 3, "name": "KeyBoard", "price": 2000},
    ]

    monkeypatch.setattr(main, "products", original_products)


# ============================================================
# 2. GET /products
# Retrieve all products with pagination
# ============================================================

def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200

    data = response.json()

    assert "products" in data
    assert len(data["products"]) == 3
    assert data["products"][0]["name"] == "Laptop"


def test_get_products_with_pagination():
    response = client.get("/products?page=1&limit=2")

    assert response.status_code == 200

    data = response.json()

    assert len(data["products"]) == 2
    assert data["products"][0]["name"] == "Laptop"
    assert data["products"][1]["name"] == "Mouse"


def test_get_products_second_page():
    response = client.get("/products?page=2&limit=2")

    assert response.status_code == 200

    data = response.json()

    assert len(data["products"]) == 1
    assert data["products"][0]["name"] == "KeyBoard"


def test_get_products_invalid_page():
    response = client.get("/products?page=0")

    assert response.status_code == 422


def test_get_products_invalid_limit():
    response = client.get("/products?limit=101")

    assert response.status_code == 422


# ============================================================
# 3. GET /products/{product_id}
# Retrieve one specific product
# ============================================================

def test_get_existing_product():
    response = client.get("/products/1")

    assert response.status_code == 200

    data = response.json()

    assert data["product"]["id"] == 1
    assert data["product"]["name"] == "Laptop"
    assert data["product"]["price"] == 50000


def test_get_nonexistent_product():
    response = client.get("/products/999")

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Product not found"
    }


def test_get_product_invalid_id_type():
    response = client.get("/products/abc")

    assert response.status_code == 422


# ============================================================
# 4. PUT /products/{product_id}
# Replace all editable product fields
# ============================================================

def test_put_update_existing_product():
    response = client.put(
        "/products/1",
        json={
            "name": "Gaming Laptop",
            "price": 75000
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Product updated successfully"
    assert data["product"]["id"] == 1
    assert data["product"]["name"] == "Gaming Laptop"
    assert data["product"]["price"] == 75000


def test_put_update_nonexistent_product():
    response = client.put(
        "/products/999",
        json={
            "name": "Tablet",
            "price": 20000
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_put_missing_required_field():
    response = client.put(
        "/products/1",
        json={
            "name": "Gaming Laptop"
        }
    )

    assert response.status_code == 422


# ============================================================
# 5. PATCH /products/{product_id}
# Update only the supplied fields
# ============================================================

def test_patch_update_price_only():
    response = client.patch(
        "/products/1",
        json={
            "price": 55000
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == (
        "Product partially updated successfully"
    )
    assert data["product"]["name"] == "Laptop"
    assert data["product"]["price"] == 55000


def test_patch_update_name_only():
    response = client.patch(
        "/products/1",
        json={
            "name": "Office Laptop"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["product"]["name"] == "Office Laptop"
    assert data["product"]["price"] == 50000


def test_patch_update_nonexistent_product():
    response = client.patch(
        "/products/999",
        json={
            "price": 10000
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_patch_invalid_price_type():
    response = client.patch(
        "/products/1",
        json={
            "price": "not-a-number"
        }
    )

    assert response.status_code == 422


# ============================================================
# 6. DELETE /products/{product_id}
# Delete a specific product
# ============================================================

def test_delete_existing_product():
    response = client.delete("/products/1")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Product deleted successfully"
    assert data["product"]["id"] == 1
    assert data["product"]["name"] == "Laptop"


def test_deleted_product_cannot_be_retrieved():
    delete_response = client.delete("/products/1")

    assert delete_response.status_code == 200

    get_response = client.get("/products/1")

    assert get_response.status_code == 404


def test_delete_nonexistent_product():
    response = client.delete("/products/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"
