from fastapi import FastAPI
from databases import Database
import logging

from api.core.config_starlette import Playarea2Config, get_playarea2_config

logger = logging.getLogger(__name__)
playarea2_config: Playarea2Config = get_playarea2_config()


async def connect_to_db(app: FastAPI) -> None:
    db = Database(playarea2_config.DB_URL, min_size=2, max_size=10)

    try:
        await db.connect()
        app.state._db = db
    except Exception as e:
        logger.warn(f'''DB CONNECTION ERROR: {e}''')


async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn(f'''DB DISCONNECTION ERROR: {e}''')
