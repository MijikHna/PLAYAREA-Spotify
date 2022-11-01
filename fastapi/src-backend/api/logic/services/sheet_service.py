
from typing import List
from fastapi import Depends

from sqlalchemy.orm import Session
from api.db.models.sheet.table_dao import TableDao
from api.db.repositories.sheet_repository import SheetRepository
from api.db.repositories.user_repository import UserRepository

from api.logic.dto.sheet_dto import CellDto, ColumnDto, RowDto, TableDto, TableInfoDto
from api.logic.dto.user_dto import UserBaseDto, UserDto


class SheetService:
    def __init__(
        self,
        sheet_repo: SheetRepository = Depends(SheetRepository),
        user_repo: UserRepository = Depends(UserRepository)
    ) -> None:
        self.__sheet_repo = sheet_repo
        self.__user_repo = user_repo

    def create_table(self, db_session: Session, new_table: TableDto, user: UserBaseDto) -> TableDto:
        new_table_in_db: TableDao = self.__sheet_repo.create_table(
            db_session, new_table, self.__user_repo.get_user_by_id(db_session, user.id))

        db_session.commit()

        return TableDto(
            id=new_table_in_db.id,
            name=new_table_in_db.name,
            columns=[ColumnDto(
                id=column.id,
                notation=column.notation,
                width=column.width,
                table_id=column.table_id,
                cells=[CellDto(
                    id=cell.id,
                    content=cell.content,
                    table_id=cell.table_id,
                    row_id=cell.row_id,
                    column_id=cell.column_id
                ) for cell in column.cells]
            ) for column in new_table_in_db.columns],
            rows=[RowDto(
                id=row.id,
                number=row.number,
                height=row.height,
                table_id=row.table_id,
                cells=[CellDto(
                    id=cell.id,
                    content=cell.content,
                    table_id=cell.table_id,
                    row_id=cell.row_id,
                    column_id=cell.column_id
                ) for cell in row.cells]
            ) for row in new_table_in_db.rows],
            cells=[CellDto(
                id=cell.id,
                content=cell.content,
                table_id=cell.table_id,
                row_id=cell.row_id,
                column_id=cell.column_id
            ) for cell in new_table_in_db.cells],
            user_id=new_table_in_db.user.id
        )

    def get_user_tables(self, db_session: Session, user: UserBaseDto) -> List[str]:
        user_tables_in_db: List[TableDao] = self.__sheet_repo.get_tables_by_user_id(
            db_session,
            user.id
        )

        return [TableInfoDto(id=table.id, name=table.name)for table in user_tables_in_db]
