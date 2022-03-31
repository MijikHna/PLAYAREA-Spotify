from pydantic import BaseSettings, validator
from functools import lru_cache

from typing import Union, Optional, Any
from pathlib import Path


class Playarea2Config(BaseSettings):
    app_name: str = 'PLAYAREA2'
    version: str = '1.0.0'
    api_prefix: str = '/api'
    spotify_client_id: str
    spotify_client_secret: str
    base_url: str
    backend_url: str
    backend_url_debug: str
    postgres_server: str
    postgres_port: int
    postgres_user: str
    postgres_user_testing: str
    postgres_password: str
    postgres_password_testing: str
    postgres_db: str
    postgres_db_testing: str
    postgres_url: str = None

    class Config:
        env_file = '.env'

    @validator('postgres_url', pre=False)
    def compound_postgres_url(cls, v, values, **kwargs):
        return f"postgresql://{values['postgres_user']}:{values['postgres_password']}@{values['postgres_server']}:{values['postgres_port']}/{values['postgres_db']}"


@lru_cache()
def get_playarea2_config() -> Playarea2Config:
    return Playarea2Config()
