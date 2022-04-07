from datetime import datetime, timedelta
import email

from typing import Optional, Dict

from fastapi import Depends
from jose import JWTError, jwt
from passlib.context import CryptContext
from api.db.models.user_dao import UserDao

from api.db.repositories.user_repository import UserRepository
from api.logic.dto.token_dto import TokenDataDto
from api.logic.dto.user_dto import UserDto, UserBaseDto
from api.shared.exceptions.incorrect_password_exception import IncorrectPasswordException
from api.shared.exceptions.user_not_found_exception import UserNotFoundException

SECRETE_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM: str = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class AuthService:
    def __init__(self, user_repo: UserRepository = Depends(UserRepository)) -> None:
        self.__user_repo = user_repo
        self.__password_context = CryptContext(
            schemes=['bcrypt'],
            deprecated='auto'
        )

    def __verify_password(self, plain_password, hashed_password):
        return self.__password_context.verify(plain_password, hashed_password)

    def __get_password_hash(self, password):
        return self.__password_context.hash(password)

    def __authenticate_user(self, user: UserDto) -> UserDto:
        user_in_db: Optional[UserDao] = self.__user_repo.get_user_by_unique_identifier(
            user)

        if user_in_db is None:
            raise UserNotFoundException

        password_ok: bool = self.__verify_password(
            user.password, user_in_db.password)

        if not password_ok:
            raise IncorrectPasswordException

        return password_ok

    def create_user_token(self, user: UserDto) -> str:
        try:
            self.__authenticate_user(user)
        except Exception as e:
            raise e
        token_data: TokenDataDto = TokenDataDto(username=user.username)
        to_encode: Dict[str:] = token_data.dict()

        expires_at: datetime = datetime.now(
        ) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode.update({'exp': expires_at})

        encoded_jwt: str = jwt.encode(
            to_encode, SECRETE_KEY, algorithm=ALGORITHM)

        return encoded_jwt

    def get_user_from_token(self, token: str) -> UserBaseDto:
        try:
            decoded_token = jwt.decode(
                token,
                SECRETE_KEY,
                algorithms=[ALGORITHM]
            )
            current_user: UserDto = UserDto(
                username=decoded_token.get('username'),
                password='temp'
            )
            found_user_in_db: UserDao = self.__user_repo.get_user_by_unique_identifier(
                current_user)
        except JWTError:
            raise UserNotFoundException
        except Exception as e:
            raise e

        user: UserBaseDto = UserBaseDto(
            id=found_user_in_db.id,
            username=found_user_in_db.username,
            email=found_user_in_db.email
        )

        return user
