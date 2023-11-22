from cProfile import Profile
from typing import List
from sqlalchemy import and_
from sqlalchemy.orm import Session

from api.db.models.user_dao import UserDao
from api.db.models.sheet.table_dao import TableDao
from api.db.models.sheet.row_dao import RowDao
from api.db.models.sheet.column_dao import ColumnDao
from api.db.models.sheet.cell_dao import CellDao
from api.logic.dto.sheet_dto import TableCreateDto, TableDto
from api.logic.dto.user_dto import UserBaseDto


class SheetRepository():
    def create_table(
        self,
        db_session: Session,
        table_options: TableCreateDto,
        user_db: UserDao,
    ) -> TableDao:
        table_db: TableDao = TableDao(
            name=table_options.name,
            user=user_db
        )

        # create rows
        for i in range(1, (table_options.rows + 1)):
            row_db: RowDao = RowDao(
                number=i,
            )

            table_db.rows.append(row_db)

        # create columns
        for i in range(0, (table_options.columns)):
            column_db: ColumnDao = ColumnDao(
                notation=chr(ord('A') + i),
            )

            table_db.columns.append(column_db)

        # create cells
        for row in table_db.rows:
            for column in table_db.columns:
                cell_db: CellDao = CellDao(
                    content=f'{row.number}{column.notation}',
                )

                column.cells.append(cell_db)
                row.cells.append(cell_db)

                table_db.cells.append(cell_db)

        db_session.add(table_db)
        db_session.flush()

        # return db_session.query(TableDao).join(RowDao).join(ColumnDao).join(CellDao).one()
        return table_db

    def get_table_by_id(table_id: int) -> TableDao:
        pass

    def update_table(table: TableDto) -> TableDao:
        pass

    def get_tables_by_user_id(self, db_session: Session, user_id: int) -> List[TableDao]:
        tables_in_db: List[TableDao] = db_session.query(
            TableDao).filter(TableDao.user_id == user_id).all()

        return tables_in_db

    def get_user_table(self, db_session: Session, id: int, user: UserBaseDto) -> TableDao:
        table_in_db: TableDao = db_session.query(TableDao).filter(
            and_(TableDao.id == id, TableDao.user_id == user.id)).one()

        return table_in_db
