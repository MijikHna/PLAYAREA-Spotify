from http.client import HTTPException
from typing import Dict, Any
import base64
from threading import Timer

import requests
from requests.models import Response
from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse, RedirectResponse

from api.core.config_fastapi import PlayareaConfig, get_playarea_config

from api.logic.dto.user_dto import UserBaseDto
from api.logic.dto.spotify_dto import SpotifyCachedUser, SpotifyCallbackCodeDto
from api.logic.dto.spotify_dto import SpotifyCallbackUserAccessTokenDto
from api.logic.services.spotify_service import SpotifyService, RENEW_TOKEN_PERIOD
from api.logic.services.user_service import UserService
from api.logic.utils.auth import get_user_from_token

from api.shared.other.other import generate_random_string
from api.shared.other.url_query_params import UrlQueryParams

playarea_config: PlayareaConfig = get_playarea_config()

spotify_router: APIRouter = APIRouter(
    prefix='/api/spotify',
    tags=['spotify'],
)


@spotify_router.get(
    '/login',
    response_class=RedirectResponse
)
async def login_to_spotify(
    user: UserBaseDto = Depends(get_user_from_token),
    spotify_service: SpotifyService = Depends(SpotifyService)
) -> JSONResponse:
    state: str = generate_random_string(16)

    auth_query_params = UrlQueryParams(
        {
            'client_id': playarea_config.spotify_client_id,
            'response_type': 'code',
            'redirect_uri': f'''{playarea_config.backend_url}/spotify/callback''',
            'state': state,
            'scope': 'streaming user-read-email user-read-private user-read-currently-playing user-read-playback-state',
            'show_dialog': 'true',
        }
    )

    spotify_user: SpotifyCachedUser = SpotifyCachedUser(
        user_id=user.id,
        spotify_login_state=state,
        user_token=None,
    )

    if not spotify_service.add_user_to_cache(spotify_user):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details='Internal Server Error'
        )

    redirect_response = JSONResponse(
        content={
            'url': 'https://accounts.spotify.com/authorize/?' + auth_query_params.to_query_str()
        },
        status_code=status.HTTP_200_OK,
    )

    return redirect_response


@spotify_router.get(
    '/callback'
)
async def login_to_spotify_callback(
    spotify_callback_code_dto: SpotifyCallbackCodeDto = Depends(),
    spotify_service: SpotifyService = Depends(SpotifyService),
    user_service: UserService = Depends(UserService)
) -> RedirectResponse:
    if spotify_callback_code_dto is not None:
        form_data: Dict[str, Any] = {
            'grant_type': 'authorization_code',
            'code': spotify_callback_code_dto.code,
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
            return RedirectResponse(url=f'''{playarea_config}/spotify/spotify-auth-error/''')

        spotify_callback_user_access_token_dto: SpotifyCallbackUserAccessTokenDto = SpotifyCallbackUserAccessTokenDto.parse_raw(
            response.content
        )

        cached_user: SpotifyCachedUser = spotify_service.find_cached_spotify_user_by_spotify_login_state(
            spotify_callback_code_dto.state
        )

        cached_user.user_token = spotify_callback_user_access_token_dto

        print((cached_user))

        spotify_service.update_cached_user(cached_user)

        app_user: UserBaseDto = user_service.find_user_by_id(
            user_id=cached_user.user_id)

        update_token_timer: Timer = Timer(
            RENEW_TOKEN_PERIOD,
            spotify_service.refresh_user_token,
            [app_user]
        )
        update_token_timer.start()

        return RedirectResponse(url=f'''{playarea_config.base_url}/spotify/login-success''')


@ spotify_router.get(
    '/get-token',
)
async def get_token(
    user: UserBaseDto = Depends(get_user_from_token),
    spotify_service: SpotifyService = Depends(SpotifyService)
) -> JSONResponse:
    try:
        cached_user: SpotifyCachedUser = spotify_service.get_user_token(user)
        user_token: str = cached_user.user_token.access_token
    except:
        return JSONResponse(content={'token:': 'Token not found'}, status_code=400)
    if user_token is None:
        return JSONResponse(content={'token:': user_token}, status_code=400)

    return JSONResponse(content={'token': user_token}, status_code=200)


@spotify_router.delete(
    '/logout',
    status_code=status.HTTP_202_ACCEPTED
)
def logout_spotify(
    user: UserBaseDto = Depends(get_user_from_token),
    spotify_service: SpotifyService = Depends(SpotifyService)
) -> None:
    return spotify_service.delete_cached_user(user)
