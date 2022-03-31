from typing import Dict, Any

from api.db.models.user_dao import UserDao
from api.logic.dto.user_dto import UserBaseDto, UserCreateDto, UserDto

from api.db.db_config import DBSession

from sqlalchemy.orm import Session
from passlib.context import CryptContext

from fastapi import Depends


def get_db():
    db: Session = DBSession()
    try:
        yield db
    except:
        db.close()


class UserRepository:
    def __init__(self, db_session: Session = Depends(get_db)) -> None:
        self.__db_session = db_session
        self.__password_context = CryptContext(
            schemes=['bcrypt'],
            deprecated='auto'
        )

    def __get_password_hash(self, password):
        return self.__password_context.hash(password)

    def create_user(
        self,
        new_user: UserCreateDto,
    ) -> UserBaseDto:
        user: UserDao = UserDao(
            id=new_user.id,
            username=new_user.username,
            email=new_user.email,
            email_verified=new_user.email_verified,
            password=self.__get_password_hash(new_user.password)
        )

        self.__db_session.add(user)
        self.__db_session.commit()

        return UserBaseDto(
            id=user.id,
            username=user.username,
            email=user.email
        )

    def get_user_by_unique_identifier(
        self,
        user: UserDto
    ) -> UserDao:
        user_in_db: UserDao = self.__db_session.query(
            UserDao
        ).filter(UserDao.username == user.username).first()

        return user_in_db
