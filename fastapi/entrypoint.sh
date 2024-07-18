#!/usr/bin/env bash

cd /app || (echo "no such directory" && exit 1)

alembic upgrade head

exec "${@}"
