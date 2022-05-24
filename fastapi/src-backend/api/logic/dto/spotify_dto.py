from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class SpotifyCallbackUserAccessTokenDto(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str


class SpotifyCallbackCodeDto(BaseModel):
    code: str
    state: str

    def verify_state(self, state: str) -> bool:
        return self.state == state


class SpotifyCachedUser(BaseModel):
    user_id: int
    spotify_login_state: Optional[str]
    user_token: Optional[SpotifyCallbackUserAccessTokenDto]
    last_token_request: Optional[datetime]
