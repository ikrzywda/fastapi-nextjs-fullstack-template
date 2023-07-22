from datetime import datetime

from pydantic import BaseModel


class IdTokenPayload(BaseModel):
    exp: datetime
    sub: str


class Token(BaseModel):
    access_token: str
    token_type: str
