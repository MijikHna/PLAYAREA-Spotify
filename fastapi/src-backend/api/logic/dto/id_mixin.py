from typing import Optional
from pydantic import BaseModel


class IdMixin(BaseModel):
    id: Optional[int]
