from typing import Optional, Dict, Any
from datetime import datetime, timedelta

from jose import JWTError, jwt
from passlib.context import CryptContext

from fastapi import Depends

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from api.core.config_fastapi import PlayareaConfig, get_playarea_config
from api.db.db_config import DBSession
from api.db.models.user_dao import UserDao
from api.db.repositories.user_repository import UserRepository
from api.logic.dto.token_dto import TokenDataDto
from api.logic.dto.user_dto import UserDto, UserBaseDto
from api.logic.utils.db_manager import open_db_session
from api.shared.exceptions.incorrect_password_exception import IncorrectPasswordException
from api.shared.exceptions.user_not_found_exception import UserNotFoundException

playarea_config: PlayareaConfig = get_playarea_config()


class AuthService:
    def __init__(self, user_repo: UserRepository = Depends(UserRepository)) -> None:
        self.__user_repo = user_repo
        self.__password_context = CryptContext(
            schemes=['bcrypt'],
            deprecated='auto'
        )

    def _verify_password(self, plain_password, hashed_password):
        return self.__password_context.verify(plain_password, hashed_password)

    def _hash_password(self, password):
        return self.__password_context.hash(password)

    def _authenticate_user(
        self,
        db_session: Session,
        user: UserDto,
    ) -> UserDto:
        try:
            user_db: Optional[UserDao] = self.__user_repo.get_user_by_unique_identifier(
                db_session,
                user
            )
        except NoResultFound:
            raise UserNotFoundException

        if user_db is None:
            raise UserNotFoundException

        if not self._verify_password(user.password, user_db.password):
            raise IncorrectPasswordException

    def create_user_token(self, db_session: Session, user: UserDto) -> str:
        try:
            self._authenticate_user(db_session, user)
        except Exception as e:
            raise e

        token_data: TokenDataDto = TokenDataDto(username=user.username)
        to_encode: Dict[str, Any] = token_data.dict()

        expires_at: datetime = datetime.now() +\
            timedelta(minutes=playarea_config.access_token_expire_minutes)

        to_encode.update({'exp': expires_at})

        encoded_jwt: str = jwt.encode(
            to_encode,
            playarea_config.secret_key,
            algorithm=playarea_config.algorithm
        )

        return encoded_jwt

    def get_user_from_token(
        self,
        db_session: Session,
        token: str,
    ) -> UserBaseDto:
        try:
            decoded_token = jwt.decode(
                token,
                playarea_config.secret_key,
                algorithms=[playarea_config.algorithm]
            )

            user: UserDto = UserDto(
                username=decoded_token.get('username'),
                password=''
            )

            user_db: UserDao = self.__user_repo.get_user_by_unique_identifier(
                db_session,
                user
            )
        except JWTError:
            raise UserNotFoundException
        except Exception as e:
            raise e

        user: UserBaseDto = UserBaseDto(
            id=user_db.id,
            username=user_db.username,
            email=user_db.email
        )

        return user
