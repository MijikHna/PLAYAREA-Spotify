from fastapi import Depends


from api.db.models.user_dao import UserDao
from api.db.repositories.user_repository import UserRepository
from api.logic.dto.user_dto import UserCreateDto, UserDto, UserBaseDto


class UserService:
    def __init__(self, user_repo: UserRepository = Depends(UserRepository)) -> None:
        self.__user_repo = user_repo

    def create_user(self, new_user_create_dto: UserCreateDto):
        new_user_dto: UserBaseDto = self.__user_repo.create_user(
            new_user=new_user_create_dto)

        return new_user_dto
