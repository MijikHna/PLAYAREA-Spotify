from fastapi import APIRouter, status, Depends, HTTPException

from fastapi.security import OAuth2PasswordRequestForm

from api.logic.dto.token_dto import TokenDto
from api.logic.dto.user_dto import UserBaseDto, UserDto
from api.logic.services.auth_service import AuthService

from api.logic.utils.auth import get_user_from_token

auth_router: APIRouter = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)


@auth_router.post(
    '/token_fastapi',
    response_model=TokenDto,
    status_code=status.HTTP_201_CREATED
)
async def create_user_token_fastapi(
    user_form: OAuth2PasswordRequestForm = Depends(
        OAuth2PasswordRequestForm),
    auth_srv: AuthService = Depends(AuthService)
) -> TokenDto:
    user: UserDto = UserDto(
        username=user_form.username,
        password=user_form.password
    )
    try:
        token: str = auth_srv.create_user_token(user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.message
        )
    return TokenDto(
        access_token=token,
        token_type='bearer'
    )


@auth_router.post(
    '/token',
    response_model=TokenDto,
    status_code=status.HTTP_201_CREATED
)
async def create_user_token(
    user: UserDto,
    auth_srv: AuthService = Depends(AuthService)
) -> TokenDto:
    try:
        token: str = auth_srv.create_user_token(user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.message
        )
    return TokenDto(
        access_token=token,
        token_type='bearer'
    )


@auth_router.get(
    '/me',
    response_model=UserBaseDto,
    status_code=status.HTTP_200_OK
)
async def get_user_from_token(user: UserBaseDto = Depends(get_user_from_token)) -> UserBaseDto:
    return user
