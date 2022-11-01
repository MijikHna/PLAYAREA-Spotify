from lib2to3.pytree import WildcardPattern
from typing import Optional, List
from api.logic.dto.id_mixin import IdMixin


class CellDto(IdMixin):
    content: str
    table_id: int
    row_id: int
    column_id: int


class RowDto(IdMixin):
    number: str
    height: int
    table_id: int
    cells: Optional[List[CellDto]]


RowDto.update_forward_refs()


class ColumnDto(IdMixin):
    notation: str
    width: int
    table_id: int
    cells: Optional[List[CellDto]]


ColumnDto.update_forward_refs()


class TableDto(IdMixin):
    name: str
    user_id: int
    rows: Optional[List[RowDto]]
    columns: Optional[List[ColumnDto]]
    cells: Optional[List[CellDto]]


TableDto.update_forward_refs()


class TableCreateDto(IdMixin):
    name: str
    rows: int
    columns: int


class TableInfoDto(IdMixin):
    name: str
