from sqlalchemy.orm import Session

from api.config.db_config import DBSession


def open_db_session():
    db: Session = DBSession()
    try:
        yield db
    except:
        db.close()
