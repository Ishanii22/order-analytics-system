from pydantic import BaseModel
from datetime import date
from typing import Optional

# ---------- Product Schemas ----------
class ProductBase(BaseModel):
    name: str
    price: float
    stock_qty: int = 0

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    model_config = {"from_attributes": True}


# ---------- Customer Schemas ----------
class CustomerBase(BaseModel):
    name: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int

    model_config = {"from_attributes": True}


# ---------- Order Item Schemas ----------
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int

    model_config = {"from_attributes": True}


# ---------- Order Schemas ----------
class OrderCreate(BaseModel):
    customer_id: int
    order_date: date
    items: list[OrderItemCreate]

class OrderResponse(BaseModel):
    id: int
    customer_id: int
    order_date: date
    status: str
    items: list[OrderItemResponse]

    model_config = {"from_attributes": True}