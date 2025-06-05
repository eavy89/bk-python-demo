from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.sqlite import get_session

SessionDep = Annotated[Session, Depends(get_session)]
