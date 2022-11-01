from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

from sqlalchemy.orm import Session

from api.logic.dto.user_dto import UserBaseDto
from api.logic.services.auth_service import AuthService
from api.logic.utils.db_manager import open_db_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/auth/token_fastapi')


async def get_user_from_token(
    token: str = Depends(oauth2_scheme),
    auth_srv: AuthService = Depends(AuthService),
    db_session: Session = Depends(open_db_session)
) -> UserBaseDto:
    try:
        user: UserBaseDto = auth_srv.get_user_from_token(db_session, token)
    except Exception as e:
        raise e

    return user
