from api.db.models.profile_dao import ProfileDao
from fastapi import Depends

from sqlalchemy.orm import Session
from api.db.db_config import DBSession

from api.db.models.user_dao import UserDao
from api.db.repositories.profile_repository import ProfileRepository
from api.db.repositories.user_repository import UserRepository
from api.logic.dto.profile_dto import ProfileDto
from api.logic.dto.user_dto import UserCreateDto, UserBaseDto, UserBaseWithProfileDto


class UserService:
    def __init__(
        self,
        user_repo: UserRepository = Depends(UserRepository),
        profile_repo: ProfileRepository = Depends(ProfileRepository)
    ) -> None:
        self.__user_repo = user_repo
        self.__profile_repo = profile_repo

    def create_user(
        self,
        db_session: Session,
        user: UserCreateDto
    ) -> UserBaseDto:
        user.profile = ProfileDto()

        try:
            user_db: UserDao = self.__user_repo.create_user(
                db_session=db_session,
                user=user,
            )

            db_session.commit()
        except Exception as e:
            raise e

        return UserBaseWithProfileDto(
            id=user_db.id,
            username=user_db.username,
            email=user_db.email,
            profile=ProfileDto(
                id=user_db.profile.id,
                theme=user_db.profile.theme,
                image=user_db.profile.image,
                user_id=user_db.profile.user_id
            )
        )

    def find_user_by_id(
        self,
        db_session: Session,
        user_id: int
    ) -> UserBaseDto:
        try:
            user_db: UserDao = self.__user_repo.get_user_by_id(
                db_session,
                user_id,
            )
        except Exception as e:
            raise e

        return UserBaseDto(
            id=user_db.id,
            username=user_db.username,
            email=user_db.email
        )
