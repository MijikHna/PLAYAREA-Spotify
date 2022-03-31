from typing import List
from pydantic import BaseModel


class SpotifyUser(BaseModel):
    user_id: int
    user_token: str


class SpotifyUsersCache:
    _instance: 'SpotifyUsersCache' = None
    cached_users: List[SpotifyUser] = []

    @staticmethod
    def get_instance():
        if SpotifyUsersCache._instance == None:
            SpotifyUsersCache()

        return SpotifyUsersCache._instance

    def __init__(self):
        if SpotifyUsersCache._instance is not None:
            return
        else:
            SpotifyUsersCache._instance = self

    def add_user_to_cache(self, token: str) -> None:
        if not self.cached_users:
            self.cached_users.append(
                SpotifyUser(
                    user_id=0,
                    user_token=token
                )
            )

            return

        self.cached_users[0] = SpotifyUser(
            user_id=0,
            user_token=token
        )

    def get_cached_user_token(self, user_id: int):
        return self.cached_users[user_id].user_token
