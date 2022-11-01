from typing import Dict, Any
from api.db.models.profile_dao import ProfileDao

from api.db.models.user_dao import UserDao
from api.logic.dto.user_dto import UserBaseDto, UserCreateDto, UserDto

from sqlalchemy.orm import Session
from passlib.context import CryptContext


class UserRepository:
    def __init__(self) -> None:
        self.__password_context = CryptContext(
            schemes=['bcrypt'],
            deprecated='auto'
        )

    def __hash_password(self, password):
        return self.__password_context.hash(password)

    def create_user(
        self,
        db_session: Session,
        user: UserCreateDto
    ) -> UserDao:
        if (user.id is not None):
            # raise
            return

        try:
            user_db: UserDao = UserDao(
                username=user.username,
                email=user.email,
                password=self.__hash_password(
                    user.password) if user.password == user.password_confirm else None,
                is_superuser=user.is_superuser,
            )

            profile_db: ProfileDao = ProfileDao(
                theme=user.profile.theme,
                image=user.profile.image,
            )
            user_db.profile = profile_db

            db_session.add(user_db)
            db_session.flush()

            profile_db.user_id = user_db.id
            db_session.add(profile_db)
            db_session.flush()
        except Exception as e:
            raise e

        return user_db

    def get_user_by_unique_identifier(
        self,
        db_session: Session,
        user_identifiers: Dict[str, Any]
    ) -> UserDao:
        # also filter for email
        user_db: UserDao = None

        if user_identifiers.email:
            user_db = db_session.query(
                UserDao
            ).filter(UserDao.email == user_identifiers.email).one()

            return user_db
        elif user_identifiers.username:
            user_db = db_session.query(
                UserDao
            ).filter(UserDao.username == user_identifiers.username).one()

            return user_db

    def get_user_by_id(
        self,
        db_session: Session,
        user_id: int
    ) -> UserDao:
        user_db = db_session.query(
            UserDao
        ).filter(UserDao.id == user_id).one()

        return user_db
