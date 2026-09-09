import uuid
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Order System API running"}


def test_create_product():
    response = client.post("/products/", json={
        "name": "Test Product",
        "price": 100.0,
        "stock_qty": 10
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 100.0
    assert "id" in data


def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_nonexistent_product():
    response = client.get("/products/99999")
    assert response.status_code == 404


def test_create_customer():
    unique_email = f"test_{uuid.uuid4().hex[:8]}@example.com"
    response = client.post("/customers/", json={
        "name": "Test Customer",
        "email": unique_email
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Customer"


def test_get_customers():
    response = client.get("/customers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)