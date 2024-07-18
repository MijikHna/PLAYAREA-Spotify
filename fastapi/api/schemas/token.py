from typing import Optional

from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str

class RefreshTokenSchema(BaseModel):
    refresh_token: str

class TokenDataSchema(BaseModel):
    id: int
    user_identifier: Optional[str] = None

class RefreshTokenDataSchema(BaseModel):
    id: int
    user_identifier: Optional[str] = None

