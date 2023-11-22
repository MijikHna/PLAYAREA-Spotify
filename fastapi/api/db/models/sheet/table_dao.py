from typing import List

from sqlalchemy import Integer, ForeignKey, String, TIMESTAMP, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from api.db.db_config import Base


class TableDao(Base):
    __tablename__ = 'sheet_tables'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    created_at: Mapped[int] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    updated_at: Mapped[int] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )

    user: Mapped['UserDao'] = relationship('UserDao', back_populates='tables')

    rows: Mapped[List['RowDao']] = relationship('RowDao', back_populates='table')
    columns :Mapped[List['ColumnDao']] = relationship('ColumnDao', back_populates='table')
    cells: Mapped[List['CellDao']] = relationship('CellDao', back_populates='table')
