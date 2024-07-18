from datetime import datetime

from sqlalchemy import TIMESTAMP, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.config.db_config import Base


class PlaybackHistoryModel(Base):
    __tablename__ = "playback_histories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    spotify_id: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    creator: Mapped[str] = mapped_column(String, nullable=False)
    # album or podcast
    context: Mapped[str] = mapped_column(String, nullable=False)
    played_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False
    )
    duration: Mapped[int] = mapped_column(Integer, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)
    image_url: Mapped[str] = mapped_column(String, nullable=False)

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    user: Mapped["UserModel"] = relationship("UserModel")
