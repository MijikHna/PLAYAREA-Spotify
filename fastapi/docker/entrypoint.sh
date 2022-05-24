#!/usr/bin/env bash
cd /app

alembic upgrade head

exec "${@}"