from threading import Timer
from typing import Dict, Any, Optional
import base64
from datetime import datetime

import requests
from requests.models import Response

from fastapi import Depends

from sqlalchemy.orm import Session


from api.core.config_fastapi import PlayareaConfig, get_playarea_config

from api.logic.dto.spotify_dto import SpotifyCachedUser
from api.logic.dto.user_dto import UserBaseDto
from api.logic.utils.spotify_users_cache import SpotifyUsersCache
from api.shared.exceptions.cached_user_not_found import CachedUserNotFound

playarea_config: PlayareaConfig = get_playarea_config()
MINUTES_5: int = 3 * 60  # 5 * 60
RENEW_TOKEN_PERIOD: int = 3 * 60  # 3600 - 3 * 60


class SpotifyService:
    def __init__(
        self,
        spotify_users_cache: SpotifyUsersCache = Depends(SpotifyUsersCache),
    ) -> None:
        self.__spotify_users_cache = spotify_users_cache

    def find_cached_spotify_user_by_spotify_login_state(
        self,
        db_session: Session,
        state: str
    ) -> Optional[SpotifyCachedUser]:
        cached_user: SpotifyCachedUser = self.__spotify_users_cache.find_cached_user_by_login_state(
            state
        )

        return SpotifyCachedUser.parse_obj(cached_user)

    def add_user_to_cache(
        self,
        db_session: Session,
        spotify_user: SpotifyCachedUser
    ) -> bool:
        # eventually throw exception
        if not spotify_user.spotify_login_state or spotify_user.user_token is not None:
            return False

        return self.__spotify_users_cache.add_user_to_cache(spotify_user)

    def update_cached_user(
        self,
        db_session: Session,
        spotify_user: SpotifyCachedUser
    ) -> bool:
        return self.__spotify_users_cache.update_cached_user(spotify_user)

    def get_user_token(self, db_session: Session, user: UserBaseDto) -> SpotifyCachedUser:
        return self.__spotify_users_cache.get_cached_user_token(user)

    def delete_cached_user(self, db_session: Session, user: UserBaseDto) -> bool:
        return self.__spotify_users_cache.delete_cached_user(user)

    def refresh_user_token(
        self,
        db_session: Session,
        user: UserBaseDto
    ):
        print('refresh started')
        if user is None:
            return False

        user_to_refresh: SpotifyCachedUser = self.__spotify_users_cache.find_cached_user_by_user_id(
            user.id
        )

        seconds_from_last_request = datetime.now() - user_to_refresh.last_token_request

        if seconds_from_last_request.seconds > MINUTES_5:
            self.__spotify_users_cache.delete_cached_user(user)
            return False

        if user_to_refresh is None:
            raise CachedUserNotFound

        form_data: Dict[str, Any] = {
            'grant_type': 'refresh_token',
            'refresh_token': user_to_refresh.user_token.refresh_token
        }

        headers: Dict[str, Any] = {
            'Authorization': 'Basic ' + base64.b64encode(bytes(f'''{playarea_config.spotify_client_id}:{playarea_config.spotify_client_secret}''', 'utf-8')).decode('utf-8'),
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response: Response = requests.post(
            'https://accounts.spotify.com/api/token',
            data=form_data,
            headers=headers
        )

        if response.status_code != requests.codes.ok:
            return False

        response_dict: Dict[str, Any] = response.json()

        user_to_refresh.user_token.access_token = response_dict['access_token']
        user_to_refresh.user_token.token_type = response_dict['token_type']
        user_to_refresh.user_token.expires_in = response_dict['expires_in']
        user_to_refresh.user_token.scope = response_dict['scope']

        result = self.__spotify_users_cache.update_cached_user(
            user=user_to_refresh)
        print(f'result: {result}')

        update_token_timer: Timer = Timer(
            RENEW_TOKEN_PERIOD,
            self.refresh_user_token,
            [user]
        )
        update_token_timer.start()

        return True
