from pydantic import BaseModel
from typing import Optional


class JWToken(BaseModel):
    access_token: str
    token_type: str


class JWTokenPayload(BaseModel):
    sub: Optional[str]