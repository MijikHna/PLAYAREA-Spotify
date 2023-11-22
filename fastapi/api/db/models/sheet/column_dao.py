from typing import List
from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    TIMESTAMP,
    func
)

from sqlalchemy.orm import relationship, Mapped, mapped_column

from api.db.db_config import Base


class ColumnDao(Base):
    __tablename__ = 'sheet_columns'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    notation: Mapped[str] = mapped_column(String, nullable=False)
    width: Mapped[int] = mapped_column(Integer, nullable=False, default=100)

    updated_at: Mapped[int] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    table_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('sheet_tables.id', ondelete='CASCADE'),
        nullable=False
    )

    table: Mapped['TableDao'] = relationship('TableDao', back_populates='columns')
    cells: Mapped[List['CellDao']] = relationship('CellDao', back_populates='column')

