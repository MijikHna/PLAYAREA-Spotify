from sqlalchemy import ForeignKey, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from api.db.db_config import Base


class CellDao(Base):
    __tablename__ = 'sheet_cells'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[String] = mapped_column(String, nullable=False)

    updated_at: Mapped[int] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    test: Mapped[int]
    table_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('sheet_tables.id', ondelete='CASCADE'),
        nullable=False
    )
    row_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('sheet_rows.id', ondelete='CASCADE'),
        nullable=False
    )
    column_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('sheet_columns.id', ondelete='CASCADE'),
        nullable=False
    )

    table: Mapped['TableDao'] = relationship('TableDao', back_populates='cells')
    row: Mapped['RowDao'] = relationship('RowDao', back_populates='cells')
    column: Mapped['ColumnDao'] = relationship('ColumnDao', back_populates='cells')
