from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import TIMESTAMP, Integer, String

from api.config.db_config import Base


class BookmarkModel(Base):
    __tablename__ = "bookmarks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    start_time: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False
    )
    end_time: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False
    )
    note: Mapped[str] = mapped_column(String, nullable=True)

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    user: Mapped["UserModel"] = relationship("UserModel")

    playback_history_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("playback_histoires.id"), nullable=False
    )
    playback_history: Mapped["PlaybackHistoryModel"] = relationship("PlaybackHistoryModel")
