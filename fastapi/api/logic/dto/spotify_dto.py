from typing import Optional, Any
from datetime import datetime, timedelta
from pydantic import BaseModel, Field


class SpotifyUserTokenDto(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str
    expires: datetime


class SpotifyCallbackDto(BaseModel):
    code: str
    state: str

    def verify_state(self, state: str) -> bool:
        return self.state == state

