from fastapi import FastAPI

from app.db.sqlite import init_sqlite_db as init_db
from app.routes.router import Router

init_db()
app = FastAPI()
app.include_router(Router)