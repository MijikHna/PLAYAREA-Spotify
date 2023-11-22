from typing import List
from sqlalchemy import (
    ForeignKey,
    Integer,
    Text,
    TIMESTAMP,
    func
)

from sqlalchemy.orm import relationship, Mapped, mapped_column

from api.db.db_config import Base


class RowDao(Base):
    __tablename__ = 'sheet_rows'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    number: Mapped[int] = mapped_column(Text, nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False, default=25)

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

    table: Mapped[List['TableDao']] = relationship('TableDao', back_populates='rows')
    cells: Mappled[List['CellDao']] = relationship('CellDao', back_populates='row')
