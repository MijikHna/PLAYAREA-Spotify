from typing import Optional

from pydantic import BaseModel


class TokenDto(BaseModel):
    access_token: str
    token_type: str


class TokenDataDto(BaseModel):
    id: int
    user_identifier: Optional[str] = None
