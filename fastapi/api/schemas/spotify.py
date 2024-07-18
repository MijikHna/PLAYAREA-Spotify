from datetime import datetime

from pydantic import BaseModel


class SpotifyUserTokenSchema(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str
    expires: datetime


class SpotifyCallbackSchema(BaseModel):
    code: str
    state: str

    def verify_state(self, state: str) -> bool:
        return self.state == state

