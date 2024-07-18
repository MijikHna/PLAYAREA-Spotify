from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from api.config.config_fastapi import PlayareaConfig, get_playarea_config

playarea_config: PlayareaConfig = get_playarea_config()

db_engine = create_engine(playarea_config.postgres_url)

DBSession: sessionmaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=db_engine
)

class Base(DeclarativeBase):
    pass
