from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.models.base import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./demo.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


def init_sqlite_db():
    Base.metadata.create_all(bind=engine)


def get_session():
    with Session(engine) as session:
        yield session
