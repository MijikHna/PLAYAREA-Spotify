import os
import base64

import requests
from requests.models import Response

from typing import Dict, Any

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse, RedirectResponse

from api.logic.services.spotify_service import SpotifyService

from api.logic.dto.spotify_dto import SpotifyCallbackCodeDto
from api.logic.dto.spotify_dto import SpotifyCallbackAccessTokenDto

from api.shared.other.other import generate_random_string
from api.shared.other.url_query_params import UrlQueryParams

spotify_router: APIRouter = APIRouter(
    prefix='/api/spotify',
    tags=['spotify'],
)


@spotify_router.get(
    '/login',
    response_class=RedirectResponse
)
async def login_to_spotify() -> RedirectResponse:
    scope: str = "streaming user-read-email user-read-private"
    state: str = generate_random_string(16)

    auth_query_params = UrlQueryParams(
        {
            'response_type': 'code',
            'client_id': os.getenv('SPOTIFY_CLIENT_ID'),
            'scope': scope,
            'redirect_uri': f'''{os.getenv('BACKEND_URL')}/spotify/callback''',
            # 'redirect_uri': f'''{os.getenv('BACKEND_URL_DEBUG')}/spotify/callback''',
            'state': state,
            'show_dialog': 'true'
        }
    )

    redirect_response = RedirectResponse(
        url='https://accounts.spotify.com/authorize/?' + auth_query_params.to_query_str(),
        status_code=status.HTTP_303_SEE_OTHER,
    )

    return redirect_response


@spotify_router.get(
    '/callback'
)
async def login_to_spotify_callback(
    spotify_callback_code_dto: SpotifyCallbackCodeDto = Depends(),
    spotify_service: SpotifyService = Depends(SpotifyService)
) -> RedirectResponse:
    print(spotify_callback_code_dto)
    spotify_auth_success: bool = False

    if spotify_callback_code_dto is not None:
        form_data: Dict[str, Any] = {
            'code': spotify_callback_code_dto.code,
            'redirect_uri': f'''{os.getenv('BACKEND_URL')}/spotify/callback''',
            # 'redirect_uri': f'''{os.getenv('BACKEND_URL_DEBUG')}/spotify/callback''',
            'grant_type': 'authorization_code'
        }

        headers: Dict[str, Any] = {
            'Authorization': 'Basic ' + base64.b64encode(bytes(f'''{os.getenv('SPOTIFY_CLIENT_ID')}:{os.getenv('SPOTIFY_CLIENT_SECRET')}''', 'utf-8')).decode('utf-8'),
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response: Response = requests.post(
            'https://accounts.spotify.com/api/token',
            data=form_data,
            headers=headers
        )

        print(response.status_code)
        if response.status_code == requests.codes.ok:
            spotify_callback_access_token_dto: SpotifyCallbackAccessTokenDto = SpotifyCallbackAccessTokenDto.parse_raw(
                response.content)
            spotify_service.save_user_token(
                spotify_callback_access_token_dto.access_token)

            print(spotify_service.get_user_token(0))

            spotify_auth_success = True

    return RedirectResponse(url=f'''{os.getenv('BASE_URL')}/spotify?spotify_auth={spotify_auth_success}''')


@spotify_router.get(
    '/get-token',
)
async def get_token(
    spotify_service: SpotifyService = Depends(SpotifyService)
) -> JSONResponse:
    try:
        user_token: str = spotify_service.get_user_token(0)
    except:
        return JSONResponse(content={'token:': 'Token not found'}, status_code=400)
    if user_token is None:
        return JSONResponse(content={'token:': user_token}, status_code=400)

    return JSONResponse(content={'token': user_token}, status_code=200)
