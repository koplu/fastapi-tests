from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_existing_order():
    response = client.get("/orders/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "product": "T-shirt",
        "quantity": 2
    }

def test_get_nonexistent_order():
    response = client.get("/orders/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"

def test_create_order():
    response = client.post(
        "/orders",
        json={"product": "Keyboard", "quantity": 1}
    )

    assert response.status_code == 201

    data = response.json()
    assert data["product"] == "Keyboard"
    assert data["quantity"] == 1
    assert isinstance(data["id"], int)

def test_create_order_with_invalid_data():
    response = client.post(
        "/orders",
        json={"product": "Keyboard", "quantity": "invalid"}
    )

    assert response.status_code == 422
