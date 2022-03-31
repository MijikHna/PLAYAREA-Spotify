from functools import lru_cache

from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import URL, Secret

config = Config('.env')


class Playarea2Config:
    APP_NAME: str = 'PLAYAREA2'
    VERSION: str = '1.0.0'
    API_PREFIX: str = '/api'
    SPOTIFY_CLIENT_ID: Secret = config('SPOTIFY_CLIENT_ID', cast=Secret)
    SPOTIFY_CLIENT_SECRET: Secret = config(
        'SPOTIFY_CLIENT_SECRET', cast=Secret)
    BASE_URL: str = config('BASE_URL', cast=URL)
    BACKEND_URL: str = config('BACKEND_URL', cast=URL)
    BACKEND_URL_DEBUG: str = config('BACKEND_URL_DEBUG', cast=URL)
    POSTGRES_SERVER: str = config(
        'POSTGRES_SERVER', cast=str, default="localhost")
    POSTGRES_PORT: str = config('POSTGRES_PORT', cast=str, default='5432')
    POSTGRES_USER: str = config('POSTGRES_USER', cast=str)
    POSTGRES_USER_TESTING: str = config('POSTGRES_USER_TESTING', cast=str)
    POSTGRES_PASSWORD: Secret = config('POSTGRES_PASSWORD', cast=Secret)
    POSTGRES_PASSWORD_TESTING: Secret = config(
        'POSTGRES_PASSWORD_TESTING', cast=Secret)
    POSTGRES_DB: str = config('POSTGRES_DB', cast=str)
    POSTGRES_DB_TESTING: str = config('POSTGRES_DB_TESTING', cast=str)
    DB_URL: DatabaseURL = config(
        'DB_URL',
        cast=DatabaseURL,
        default=f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}',
    )
    DB_URL_TESTING: DatabaseURL = config(
        'DB_URL_TESTING',
        cast=DatabaseURL,
        default=f'postgresql://{POSTGRES_USER_TESTING}:{POSTGRES_PASSWORD_TESTING}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB_TESTING}',
    )


@lru_cache()
def get_playarea2_config() -> Playarea2Config:
    return Playarea2Config()
