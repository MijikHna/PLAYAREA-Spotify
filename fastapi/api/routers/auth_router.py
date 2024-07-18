from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.schemas.token import RefreshTokenSchema, TokenSchema
from api.schemas.user import LoggedInUserDto, LoginUserDto
from api.services.auth.auth_service import AuthService, retrieve_user_from_token
from api.utils.db_manager import open_db_session
from fastapi import APIRouter, Depends, HTTPException, status

auth_router: APIRouter = APIRouter(prefix="/api/auth", tags=["auth"])


@auth_router.post(
    "/token_fastapi", response_model=TokenSchema, status_code=status.HTTP_201_CREATED
)
async def create_user_token_fastapi(
    user_form: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    auth_srv: AuthService = Depends(AuthService),
    db_session: Session = Depends(open_db_session),
) -> TokenSchema:
    user: LoginUserDto = LoginUserDto(
        login_identifier=user_form.username, password=user_form.password
    )
    try:
        token: TokenSchema = auth_srv.create_user_token(db_session, user)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    return token


@auth_router.post(
    "/token", response_model=TokenSchema, status_code=status.HTTP_201_CREATED
)
async def create_user_token(
    user_login: LoginUserDto,
    auth_srv: AuthService = Depends(AuthService),
    db_session: Session = Depends(open_db_session),
) -> TokenSchema:
    try:
        token: TokenSchema = auth_srv.create_user_token(db_session, user_login)
        print(token)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    return token


@auth_router.get("/me", response_model=LoggedInUserDto, status_code=status.HTTP_200_OK)
async def get_user_from_token(
    logged_in_user: LoggedInUserDto = Depends(retrieve_user_from_token),
) -> LoggedInUserDto:
    return logged_in_user


@auth_router.post("/token_renew")
async def renew_user_token(
    refresh_token: RefreshTokenSchema,
    auth_service: AuthService = Depends(AuthService),
    db_session: Session = Depends(open_db_session),
) -> TokenSchema:
    try:
        token: TokenSchema = auth_service.renew_token(
            refresh_token.refresh_token, db_session
        )
        return token
    except Exception as e:
        raise e


@auth_router.post("/logout")
async def logout_user(
    logged_in_user: LoggedInUserDto = Depends(retrieve_user_from_token),
    auth_service: AuthService = Depends(AuthService),
    db_session: Session = Depends(open_db_session),
) -> None:
    try:
        pprint
        auth_service.logout_user(logged_in_user.id, db_session)
    except Exception as e:
        raise e
