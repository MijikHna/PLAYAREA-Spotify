from typing import List, Optional
from pydantic import BaseModel

# General

class BaseProfileDto(BaseModel):
    id: int
    dark_theme: bool
    active_image: Optional[str] = None
    images: Optional[List[str]] = None

# Get
class GetProfileDto(BaseModel):
    id: int
    dark_theme: bool
    active_image: Optional[str] = None
    images: Optional[List[str]] = None
    user_id: Optional[int]

# TODO: Validation theme (default: light), image (default: no_picture.png)

# Put/Patch
class PutProfileDto(BaseModel):
    id: int
    dark_theme: bool
    active_image: str
