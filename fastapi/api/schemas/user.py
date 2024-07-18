from typing import Optional

from pydantic import BaseModel

from api.schemas.profile import GetProfileDto


# TODO: move to separate file
class LoginUserDto(BaseModel):
    login_identifier: str
    password: str


class LoggedInUserDto(BaseModel):
    id: int
    username: Optional[str] = None
    email: str

# Get
class GetUserEmailAndUsernameDto(BaseModel):
    email: str
    username: str


class GetUserWithProfile(BaseModel):
    username: str
    email: str
    profile: GetProfileDto

# Post
class CreateUserDto(BaseModel):
    username: str
    email: str
    email_verified: bool = False
    password: str
    password_confirm: str
    is_superuser: bool = False

# Put / Patch
class EditUserDto(BaseModel):
    email_verified: str
    password: str
    is_active: bool
    is_superuser: bool

# Delete
