"""create history and bookmark tables

Revision ID: a48208b1e278
Revises: 550e3520b3fc
Create Date: 2024-07-03 15:28:08.099709

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic
revision = "a48208b1e278"
down_revision = "550e3520b3fc"
branch_labels = None
depends_on = None


def create_playback_histories_table() -> None:
    op.create_table(
        "playback_histories",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("spotify_id", sa.Text, nullable=False),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("creator", sa.Text, nullable=False),
        sa.Column("context", sa.Text, nullable=False),
        sa.Column("played_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("duration", sa.Integer, nullable=False),
        sa.Column("url", sa.Text, nullable=False),
        sa.Column("image_url", sa.Text, nullable=False),
        sa.Column(
            "user_id",
            sa.Integer,
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
    )


def create_bookmarks_table() -> None:
    op.create_table(
        "bookmarks",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("start_time", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("end_time", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("note", sa.Text, nullable=True),
        sa.Column(
            "user_id",
            sa.Integer,
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "playback_history_id",
            sa.Integer,
            sa.ForeignKey("playback_histories.id"),
            nullable=False,
        ),
    )


def upgrade() -> None:
    create_playback_histories_table()
    create_bookmarks_table()


def downgrade() -> None:
    op.drop_table("bookmarks")
    op.drop_table("playback_histories")

