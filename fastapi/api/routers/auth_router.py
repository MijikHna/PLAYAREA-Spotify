from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from api.logic.dto.token_dto import TokenDto
from api.logic.dto.user_dto import LoggedInUserDto, LoginUserDto
from api.logic.utils.auth_service import AuthService, retrieve_user_from_token

from api.logic.utils.db_manager import open_db_session

auth_router: APIRouter = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)

@auth_router.post('/token_fastapi', response_model=TokenDto, status_code=status.HTTP_201_CREATED)
async def create_user_token_fastapi(
    user_form: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    auth_srv: AuthService = Depends(AuthService),
    db_session: Session = Depends(open_db_session)
) -> TokenDto:
    user: LoginUserDto = LoginUserDto(
        login_identifier=user_form.username, 
        password=user_form.password
    )
    try:
        token: str = auth_srv.create_user_token(db_session, user)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    return TokenDto(access_token=token, token_type='bearer')


@auth_router.post('/token', response_model=TokenDto, status_code=status.HTTP_201_CREATED)
async def create_user_token(
    user_login: LoginUserDto,
    auth_srv: AuthService = Depends(AuthService),
    db_session: Session = Depends(open_db_session)
) -> TokenDto:
    try:
        token: str = auth_srv.create_user_token(db_session, user_login)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    return TokenDto(access_token=token, token_type='bearer')


@auth_router.get('/me', response_model=LoggedInUserDto, status_code=status.HTTP_200_OK)
async def get_user_from_token(
    logged_in_user: LoggedInUserDto = Depends(retrieve_user_from_token)
) -> LoggedInUserDto:
    return logged_in_user
