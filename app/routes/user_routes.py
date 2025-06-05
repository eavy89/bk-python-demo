from fastapi import Depends, HTTPException, Header, Security
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from app.auth import auth
from app.auth.dependencies import get_token_payload
from app.auth.jwt_handler import create_access_token, decode_access_token
from app.routes.base_routers import public_router, protected_router
from app.schemas import UserOut, UserCreate, UserLogin, TokenData
from app.db import SessionDep
from app.models import User
from app.schemas.token_schema import Token


@public_router.post("/register", response_model=UserOut)
def register(db: SessionDep, user: UserCreate):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_pw = auth.get_password_hash(user.password)
    new_user = User(username=user.username, password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@public_router.post("/login", response_model=Token)
def login(db: SessionDep, user: Annotated[OAuth2PasswordRequestForm, Depends()]):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"}
                            )

    token_data = {
        "user_id": int(db_user.id),
        "username": db_user.username,
    }

    access_token = create_access_token(token_data)
    return {"access_token": access_token, "token_type": "bearer"}


@protected_router.get("/profile", response_model=UserOut)
def profile(db: SessionDep, data: TokenData = Depends(get_token_payload)):
    user = db.query(User).get(data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
