import pathlib
import sys

import alembic

from sqlalchemy import engine_from_config, pool

from logging.config import fileConfig
import logging

# append the app directory to the path here so that config can be imported easily
# sys.path.append(str(pathlib.Path(__file__).resolve().parents[3]))
# from api.core.config import DATABASE_URL

# append the app directory to the path here so that config can be imported easily
sys.path.append(str(pathlib.Path(__file__).resolve().parents[3]))

from api.core.config_fastapi import PlayareaConfig, get_playarea_config


playarea_config: PlayareaConfig = get_playarea_config()

# Alembic Config object, which provides access to values within the .ini file
alembic_config = alembic.context.config


# Interpret the config file for logging
fileConfig(alembic_config.config_file_name)
logger = logging.getLogger("alembic.env")


def run_migrations_online() -> None:
    """
    Run migrations in 'online' mode
    """
    connectable = alembic_config.attributes.get("connection", None)
    alembic_config.set_main_option(
        "sqlalchemy.url",
        str(playarea_config.postgres_url)
    )

    if connectable is None:
        connectable = engine_from_config(
            alembic_config.get_section(alembic_config.config_ini_section),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
        )

    with connectable.connect() as connection:
        alembic.context.configure(
            connection=connection,
            target_metadata=None
        )

        with alembic.context.begin_transaction():
            alembic.context.run_migrations()


def run_migrations_offline() -> None:
    """
    Run migrations in 'offline' mode.
    """
    alembic.context.configure(url=str(playarea_config.postgres_url))

    with alembic.context.begin_transaction():
        alembic.context.run_migrations()


if alembic.context.is_offline_mode():
    logger.info("Running migrations offline")
    run_migrations_offline()
else:
    logger.info("Running migrations online")
    run_migrations_online()
