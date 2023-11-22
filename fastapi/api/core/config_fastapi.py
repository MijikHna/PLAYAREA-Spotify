from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field
from functools import lru_cache


class PlayareaConfig(BaseSettings):
    app_name: str = 'PLAYAREA2'
    version: str = '1.0.0'
    api_prefix: str = '/api'
    spotify_client_id: str
    spotify_client_secret: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    base_url: str
    backend_url: str
    postgres_server: str
    postgres_port: int
    postgres_user: str
    postgres_user_testing: str
    postgres_password: str
    postgres_password_testing: str
    postgres_db: str
    postgres_db_testing: str

    @computed_field
    @property
    def postgres_url(self) -> str:
        return f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}@{self.postgres_server}:{self.postgres_port}/{self.postgres_db}"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

@lru_cache()
def get_playarea_config() -> PlayareaConfig:
    return PlayareaConfig()
