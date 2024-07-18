#!/usr/bin/env bash
if [ ! -d /app/node_modules ]; then
    cd /app
    npm install
fi

cd /app
exec "${@}"