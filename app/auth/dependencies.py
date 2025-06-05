from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.auth.jwt_handler import decode_access_token
from app.schemas import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_token_payload(token: str = Depends(oauth2_scheme)) -> TokenData:
    return decode_access_token(token)
