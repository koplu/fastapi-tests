import httpx

def test_get_order_over_http():
    response = httpx.get(
        "http://127.0.0.1:8000/orders/1",
        timeout=5.0
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "product": "T-shirt",
        "quantity": 2
    }