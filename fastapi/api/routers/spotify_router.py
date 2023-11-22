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
    db_session: Session = Depends(open_db_session)
) -> JSONResponse:
    query_params = spotify_service.login_to_spotify(user)

    return JSONResponse(
        content={
            'url': f'https://accounts.spotify.com/authorize/?{query_params.to_query_str()}'
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
    print(user_token)

    if user_token is None:
        return JSONResponse(content={'token:': 'Token not found'}, status_code=400)

    return JSONResponse(content={'token': user_token.access_token}, status_code=200)


@spotify_router.delete('/logout', status_code=status.HTTP_202_ACCEPTED)
def logout_spotify(
    user: LoggedInUserDto = Depends(retrieve_user_from_token),
    spotify_service: SpotifyService = Depends(SpotifyService),
) -> bool:
    return spotify_service.logout_from_spotify(user_id=user.id)
