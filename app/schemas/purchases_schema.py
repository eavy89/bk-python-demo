from typing import List

from pydantic import BaseModel


class PurchaseIn(BaseModel):
    name: str
    price: float
    quantity: int


class PurchaseCreate(BaseModel):
    items: List[PurchaseIn]


class PurchaseOut(BaseModel):
    name: str
    price: float
    quantity: int
    timestamp: str


class PurchaseResponse(BaseModel):
    items: List[PurchaseOut]

    class Config:
        from_attributes = True
