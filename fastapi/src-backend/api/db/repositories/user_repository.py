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

    def __hash_password(self, password):
        return self.__password_context.hash(password)

    def create_user(
        self,
        new_user: UserCreateDto,
    ) -> UserDao:
        user: UserDao = UserDao(
            id=new_user.id,
            username=new_user.username,
            email=new_user.email,
            email_verified=new_user.email_verified,
            password=self.__hash_password(new_user.password)
        )

        self.__db_session.add(user)
        self.__db_session.commit()

        return user

    def get_user_by_unique_identifier(
        self,
        user: UserDto
    ) -> UserDao:
        # also filter for email
        user_in_db: UserDao = self.__db_session.query(
            UserDao
        ).filter(UserDao.username == user.username).one()

        return user_in_db

    def get_user_by_id(
        self,
        user_id: UserBaseDto,
    ) -> UserDao:
        user_in_db: UserDao = self.__db_session.query(
            UserDao
        ).filter(UserDao.id == user_id).one()

        return user_in_db
