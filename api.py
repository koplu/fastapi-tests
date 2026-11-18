
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

orders = {
    1: {"id": 1, "product": "T-shirt", "quantity": 2}
}

class OrderCreate(BaseModel):
    product: str
    quantity: int

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")

    return orders[order_id]

@app.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    new_id = max(orders.keys(), default=0) + 1

    new_order = {
        "id": new_id,
        "product": order.product,
        "quantity": order.quantity
    }

    orders[new_id] = new_order
    return new_order
