from api.db.db_config import DBSession

from sqlalchemy.orm import Session


def open_db_session():
    db: Session = DBSession()
    try:
        yield db
    except:
        db.close()
