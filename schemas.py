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

    class Config:
        from_attributes = True


# ---------- Customer Schemas ----------
class CustomerBase(BaseModel):
    name: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int

    class Config:
        from_attributes = True