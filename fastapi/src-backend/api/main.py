from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routers.base_router import base_router
from api.routers.user_router import user_router
from api.routers.auth_router import auth_router
from api.routers.spotify_router import spotify_router

from api.core.config_starlette import Playarea2Config, get_playarea2_config
from api.core.tasks import create_start_app_handler, create_stop_app_handler

playarea2_config: Playarea2Config = get_playarea2_config()

app: FastAPI = FastAPI(
    title=playarea2_config.APP_NAME,
    version=playarea2_config.VERSION
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # expose_headers=["*"],
    # max_age=3600
)

app.add_event_handler('startup', create_start_app_handler(app))
app.add_event_handler('shutdown', create_stop_app_handler(app))

app.include_router(spotify_router)
app.include_router(base_router)
app.include_router(user_router)
app.include_router(auth_router)
