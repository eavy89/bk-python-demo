from fastapi import APIRouter
from fastapi.params import Depends

from app.auth.dependencies import oauth2_scheme

# Shared routers
public_router = APIRouter(tags=["public"])
protected_router = APIRouter(prefix="/api", tags=["api"], dependencies=[Depends(oauth2_scheme)])
