from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from api.core.config_fastapi import PlayareaConfig, get_playarea_config


playarea_config: PlayareaConfig = get_playarea_config()
db_engine = create_engine(playarea_config.postgres_url)

DBSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=db_engine
)


def get_db():
    db: Session = DBSession()
    try:
        yield db
    except:
        db.close()
