from fastapi import Depends

from api.logic.utils.spotify_users_cache import SpotifyUsersCache


class SpotifyService:
    def __init__(self, spotify_users_cache: SpotifyUsersCache = Depends(SpotifyUsersCache)) -> None:
        self._spotify_users_cache = spotify_users_cache

    def save_user_token(self, token: str):
        self._spotify_users_cache.add_user_to_cache(token)

    def get_user_token(self, user_id: int):
        return self._spotify_users_cache.get_cached_user_token(user_id)
