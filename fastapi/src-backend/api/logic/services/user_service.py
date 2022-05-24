from fastapi import Depends

from api.db.models.user_dao import UserDao
from api.db.repositories.user_repository import UserRepository
from api.logic.dto.user_dto import UserCreateDto, UserBaseDto


class UserService:
    def __init__(self, user_repo: UserRepository = Depends(UserRepository)) -> None:
        self.__user_repo = user_repo

    def create_user(self, new_user_create_dto: UserCreateDto) -> UserBaseDto:
        new_user_in_db: UserDao = self.__user_repo.create_user(
            new_user=new_user_create_dto)

        return UserBaseDto(
            id=new_user_in_db.id,
            username=new_user_create_dto.username,
            email=new_user_in_db.email
        )

    def find_user_by_id(self, user_id: int) -> UserBaseDto:
        user_in_db: UserDao = self.__user_repo.get_user_by_id(user_id)

        return UserBaseDto(
            id=user_in_db.id,
            username=user_in_db.username,
            email=user_in_db.email
        )
