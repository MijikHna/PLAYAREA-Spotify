from datetime import datetime
from typing import List, Optional

from api.logic.dto.spotify_dto import SpotifyCachedUser
from api.logic.dto.user_dto import UserBaseDto


class SpotifyUsersCache:
    _instance: 'SpotifyUsersCache' = None
    __cached_users: List[SpotifyCachedUser] = []

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

    def find_cached_user_by_login_state(self, state: str) -> Optional[SpotifyCachedUser]:
        for user in self.__cached_users:
            if (user.spotify_login_state == state):
                return SpotifyCachedUser.parse_obj(user)

        return None

    def find_cached_user_by_user_id(self, user_id: int) -> Optional[SpotifyCachedUser]:
        for user in self.__cached_users:
            if (user.user_id == user_id):
                return SpotifyCachedUser.parse_obj(user)

        return None

    def update_cached_user(self, user: SpotifyCachedUser) -> bool:
        if user.user_token is None:
            return False

        for cached_user in self.__cached_users:
            if (cached_user.user_id == user.user_id):
                print(user.user_token.access_token)

                cached_user.spotify_login_state = None
                cached_user.user_token = user.user_token

                print(cached_user.user_token.access_token)
                print(len(self.__cached_users))

                return True

        return False

    def add_user_to_cache(
        self,
        user: SpotifyCachedUser
    ) -> bool:
        self.__cached_users.append(user)

        return True

    def get_cached_user_token(self, user: UserBaseDto) -> Optional[SpotifyCachedUser]:
        for cached_user in self.__cached_users:
            if cached_user.user_id == user.id:
                cached_user.last_token_request = datetime.now()
                return SpotifyCachedUser.parse_obj(cached_user)

        return None

    def delete_cached_user(self, user: UserBaseDto) -> bool:
        for cached_user in self.__cached_users:
            if cached_user.user_id == user.id:
                self.__cached_users.remove(cached_user)

                print(len(self.__cached_users))

                return True

        # eventually User not Found Exception
        return False
