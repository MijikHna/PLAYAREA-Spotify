from typing import Optional

from pydantic import BaseModel


class TokenDto(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str

class ReqRefreshToken(BaseModel):
    refresh_token: str

class TokenDataDto(BaseModel):
    id: int
    user_identifier: Optional[str] = None

class RefreshtokenDataDto(BaseModel):
    id: int
    user_identifier: Optional[str] = None

