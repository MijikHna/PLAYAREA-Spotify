from fastapi import FastAPI
from api.db.db_config import db_engine
from sqlalchemy.engine import Connection
import logging

logger = logging.getLogger(__name__)


async def connect_to_db(app: FastAPI) -> None:
    try:
        conn: Connection = db_engine.connect()
        app.state._db_engine = conn
    except Exception as e:
        logger.warn(f'''DB CONNECTION ERROR: {e}''')


async def close_db_connection(app: FastAPI) -> None:
    try:
        conn: Connection = app.state._db_engine
        conn.close()
    except Exception as e:
        logger.warn(f'''DB DISCONNECTION ERROR: {e}''')
