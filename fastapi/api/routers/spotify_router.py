from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse, RedirectResponse

from sqlalchemy.orm import Session

from api.core.config_fastapi import PlayareaConfig, get_playarea_config

from api.logic.dto.user_dto import LoggedInUserDto
from api.logic.dto.spotify_dto import SpotifyCallbackDto
from api.logic.services.spotify_service import SpotifyService
from api.logic.utils.auth_service import retrieve_user_from_token 
from api.logic.utils.db_manager import open_db_session

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
    user: LoggedInUserDto = Depends(retrieve_user_from_token),
    spotify_service: SpotifyService = Depends(SpotifyService),
) -> JSONResponse:
    login_query_params: str = spotify_service.prepare_spotify_login_url_params(user)

    return JSONResponse(
        content={
            'url': f'https://accounts.spotify.com/authorize/?{login_query_params}'
        },
        status_code=status.HTTP_200_OK,
    )


@spotify_router.get(
    '/callback'
)
async def login_to_spotify_callback(
    spotify_callback_code_dto: SpotifyCallbackDto = Depends(),
    spotify_service: SpotifyService = Depends(SpotifyService),
) -> RedirectResponse:
    try:
        spotify_service.handle_login_to_spotify_callback(spotify_callback_code_dto)
    except:
        return RedirectResponse(url=f'{playarea_config.base_url}/spotify/login-failure')

    return RedirectResponse(url=f'{playarea_config.base_url}/spotify/player')


@ spotify_router.get('/get-token')
async def get_token(
    user: LoggedInUserDto = Depends(retrieve_user_from_token),
    spotify_service: SpotifyService = Depends(SpotifyService),
) -> JSONResponse:
    user_token = spotify_service.get_user_token(user_id=user.id)
    print('get-token', user_token)

    if user_token is None:
        return JSONResponse(content={'token:': None}, status_code=200)

    return JSONResponse(content={
        'token': user_token.access_token, 
        'expires_in': user_token.expires_in
    }, status_code=200)

@spotify_router.get('/refresh-token')
async def refresh_token(
    user: LoggedInUserDto = Depends(retrieve_user_from_token),
    spotify_service: SpotifyService = Depends(SpotifyService),
) -> JSONResponse:
    user_token = spotify_service.refresh_token(user_id=user.id)
    print(user_token)

    if user_token is None:
        return JSONResponse(content={'token:': None}, status_code=200)

    return JSONResponse(content={
        'token': user_token.access_token, 
        'expires_in': user_token.expires_in
    }, status_code=200)


@spotify_router.delete('/logout', status_code=status.HTTP_202_ACCEPTED)
def logout_spotify(
    user: LoggedInUserDto = Depends(retrieve_user_from_token),
    spotify_service: SpotifyService = Depends(SpotifyService),
) -> bool:
    return spotify_service.logout_from_spotify(user_id=user.id)
