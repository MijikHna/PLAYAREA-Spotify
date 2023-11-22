from typing import Any, List, Optional

from pydantic import BaseModel

class SpotifyUser(BaseModel):
    user_id: int
    state: str
    token: Optional[Any] = None



class SpotifyUsersCache:
    _instance: Optional['SpotifyUsersCache'] = None
    spotify_users: List[SpotifyUser] = []

    @staticmethod
    def get_instance():
        if SpotifyUsersCache._instance == None:
            SpotifyUsersCache()

        return SpotifyUsersCache._instance

    def __init__(self):
        if SpotifyUsersCache._instance is not None:
            return
        SpotifyUsersCache._instance = self

    def add_user(self, user_id: int, state: str) -> bool:
        # Check if user already exists
        user_exists: SpotifyUser = None

        for user in self.spotify_users:
            if user.user_id == user_id:
                user_exists = user

        if not user_exists:
            self.spotify_users.append(SpotifyUser(user_id=user_id, state=state))
        else :
            user_exists.state = state
            user_exists.token = None

        return True

    def add_user_token(self, user_id: int, token) -> bool:
        for user in self.spotify_users:
            if user.user_id == user_id and user.state == token.state:
                user.token = token
                print(self.spotify_users)
                return True

        return False

    def delete_user(self, user_id: int) -> bool:
        for user in self.spotify_users:
            if user.user_id == user_id:
                self.spotify_users.remove(user)
                print(self.spotify_users)
                return True
        
        return False
