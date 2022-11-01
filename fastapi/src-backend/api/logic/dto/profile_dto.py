from typing import List, Optional
from api.logic.dto.id_mixin import IdMixin


class ProfileDto(IdMixin):
    theme: str = 'light'
    theme_options: Optional[List[str]]
    image: Optional[str]
    image_options: Optional[List[str]]
    user_id: Optional[int]

# TODO: Validation theme (default: light), image (default: no_picture.png)
