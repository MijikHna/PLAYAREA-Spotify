from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from api.logic.dto.user_dto import UserBaseDto

from api.logic.services.auth_service import AuthService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/auth/token')


async def get_user_from_token(
    token: str = Depends(oauth2_scheme),
    auth_srv: AuthService = Depends(AuthService)
) -> UserBaseDto:

    try:
        user: UserBaseDto = auth_srv.get_user_from_token(token)
    except Exception as e:
        raise e

    return user
