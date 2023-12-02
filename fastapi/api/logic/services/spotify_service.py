from typing import Dict, Any, Optional, List, Tuple
import base64
from datetime import datetime, timedelta

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
    
    def prepare_spotify_login_url_params(self, user: LoggedInUserDto) -> str:
        state: str = generate_random_string(16)
        
        query_params = f'''client_id={playarea_config.spotify_client_id}&response_type=code&redirect_uri={playarea_config.backend_url}/spotify/callback&state={state}&scope=streaming user-read-email user-read-private user-read-currently-playing user-read-playback-state user-library-read user-follow-read user-top-read&show_dialog=true'''

        self.__spotify_users.add_user(user_id=user.id, state=state)

        return query_params

    def handle_login_to_spotify_callback(self, callback_code: SpotifyCallbackDto) -> None:
        # find user in cache
        spotify_user: Optional[SpotifyUser] = next((user for user in self.__spotify_users.spotify_users if user.state == callback_code.state), None)

        if spotify_user is None:
            print('User not found')
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
        
        print('response', response.content)

        user_token = SpotifyUserTokenDto(**response.json(), expires=datetime.now() + timedelta(seconds=response.json()['expires_in'] - 20))
        spotify_user.token = user_token
        print('token', user_token)

        print (spotify_user)

    def get_user_token(self, user_id: int) -> Optional[SpotifyUserTokenDto]:
        # find user in cache check if token is expired and refresh if needed
        user: Optional[SpotifyUser] = next((user for user in self.__spotify_users.spotify_users if user.user_id == user_id), None)
        
        print('get_token', user)
        if user and user.token:
            if user.token.expires < datetime.now():
                print('refreshing token')
                user = self.refresh_token(user_id=user_id)

            print(user)
            return user.token

        return None

    def refresh_token(self, user_id: int) -> SpotifyUser:
        spotify_user: Optional[SpotifyUser] = next((user for user in self.__spotify_users.spotify_users if user.user_id == user_id), None)

        if spotify_user is None:
            raise CachedUserNotFound()

        # get token
        form_data: Dict[str, Any] = {
            'grant_type': 'refresh_token',
            'refresh_token': spotify_user.token.refresh_token,
            'client_id': playarea_config.spotify_client_id,
        }

        headers: Dict[str, Any] = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + base64.b64encode(bytes(f'''{playarea_config.spotify_client_id}:{playarea_config.spotify_client_secret}''', 'utf-8')).decode('utf-8'),
        }

        response: Response = requests.post(
            'https://accounts.spotify.com/api/token',
            params = form_data,
            headers=headers
        )

        if response.status_code != requests.codes.ok:
            raise Exception('Failed to get token from spotify')
        
        print(response.content)

        spotify_user.token.access_token = response.json()['access_token']
        spotify_user.token.expires_in = response.json()['expires_in']
        spotify_user.token.expires = datetime.now() + timedelta(seconds=response.json()['expires_in'] - 20)
        spotify_user.token.scope = response.json()['scope']
        spotify_user.token.token_type = response.json()['token_type']

        return spotify_user


    def logout_from_spotify(self, user_id: int) -> bool:
        return self.__spotify_users.delete_user(user_id=user_id)


