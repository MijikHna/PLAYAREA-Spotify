from typing import Dict, Any, Optional, List, Tuple
import base64

import requests
from requests.models import Response

from api.core.config_fastapi import PlayareaConfig, get_playarea_config

from api.logic.dto.spotify_dto import SpotifyCallbackDto, SpotifyUserTokenDto
from api.logic.dto.user_dto import LoggedInUserDto
from api.logic.utils.spotify_users_cache import SpotifyUser, SpotifyUsersCache
from api.shared.exceptions.cached_user_not_found import CachedUserNotFound
from api.shared.other.url_query_params import UrlQueryParams
from api.shared.other.other import generate_random_string

playarea_config: PlayareaConfig = get_playarea_config()

class SpotifyService:
    __spotify_users: SpotifyUsersCache

    def __init__(
        self,
    ) -> None:
        self.__spotify_users = SpotifyUsersCache.get_instance()
    
    def login_to_spotify(self, user: LoggedInUserDto) -> UrlQueryParams:
        state: str = generate_random_string(16)
        
        auth_query_params = UrlQueryParams({
            'client_id': playarea_config.spotify_client_id,
            'response_type': 'code',
            'redirect_uri': f'''{playarea_config.backend_url}/spotify/callback''',
            'state': state,
            'scope': 'streaming user-read-email user-read-private user-read-currently-playing user-read-playback-state user-library-read user-follow-read',
            'show_dialog': 'true',
        })

        self.__spotify_users.add_user(user_id=user.id, state=state)

        return auth_query_params

    def handle_login_to_spotify_callback(self, callback_code: SpotifyCallbackDto) -> None:
        # find user in cache
        spotify_user: SpotifyUser = None
        for user in self.__spotify_users.spotify_users:
            if user.state == callback_code.state:
                spotify_user = user
                break

        if spotify_user is None:
            raise CachedUserNotFound()

        # get token
        form_data: Dict[str, Any] = {
            'grant_type': 'authorization_code',
            'code': callback_code.code,
            'redirect_uri': f'''{playarea_config.backend_url}/spotify/callback'''
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
            raise Exception('Failed to get token from spotify')
        
        print(response.content)

        user_token = SpotifyUserTokenDto(**response.json())
        spotify_user.token = user_token

        print (spotify_user)

    def get_user_token(self, user_id: int) -> Optional[SpotifyUserTokenDto]:
        for user in self.__spotify_users.spotify_users:
            print(user)
            if user.user_id == user_id:
                return user.token

        return None

    def logout_from_spotify(self, user_id: int) -> bool:
        return self.__spotify_users.delete_user(user_id=user_id)


