from typing import Optional
from api.logic.dto.id_mixin import IdMixin
from api.logic.dto.profile_dto import ProfileDto


class UserDto(IdMixin):
    username: Optional[str]
    email: Optional[str]
    password: str


class UserBaseDto(IdMixin):
    username: str
    email: str


class UserBaseWithProfileDto(UserBaseDto):
    profile: ProfileDto


class UserCreateDto(UserBaseDto):
    email_verified: bool = False
    password: str
    password_confirm: str
    is_superuser: bool = False
    profile: Optional[ProfileDto]


class UserEditDto(UserBaseDto):
    email_verified: str
    password: str
    is_active: bool
    is_superuser: bool
