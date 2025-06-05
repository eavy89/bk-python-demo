from fastapi import APIRouter
from .base_routers import public_router, protected_router
from . import user_routes, purchases_routes  # just importing them registers routes (it must be)

Router = APIRouter()
Router.include_router(public_router)
Router.include_router(protected_router)
