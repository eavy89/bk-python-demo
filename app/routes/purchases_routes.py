from datetime import datetime, timezone
from typing import List

from fastapi import Depends

from app.auth.dependencies import get_token_payload
from app.routes.base_routers import protected_router
from app.schemas import PurchaseOut, PurchaseCreate, TokenData
from app.models import Purchase
from app.db import SessionDep
from app.schemas.purchases_schema import PurchaseResponse


@protected_router.get("/purchases", response_model=list[PurchaseOut])
def get_purchases(db: SessionDep, data: TokenData = Depends(get_token_payload)):
    purchases = db.query(Purchase).filter(Purchase.owner_id == data.user_id).all()
    return purchases


@protected_router.post("/purchases", response_model=PurchaseResponse)
def add_purchase(db: SessionDep, purchase: PurchaseCreate, data: TokenData = Depends(get_token_payload)):
    new_purchases: List[Purchase] = []
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    for item in purchase.items:
        new_purchase = Purchase(name=item.name, price=item.price, quantity=item.quantity, timestamp=timestamp, owner_id=data.user_id)
        db.add(new_purchase)
        new_purchases.append(new_purchase)

    db.commit()

    return PurchaseResponse(items=[
        PurchaseOut(name=p.name, price=p.price, quantity=p.quantity, timestamp=p.timestamp) for p in new_purchases
    ])
