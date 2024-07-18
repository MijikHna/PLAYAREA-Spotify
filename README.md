# PLAYAREA

## PURPOSE

There are a couple of things that I am missing in actual Spotify App.

1. I want to have a proper podcast history
2. I want to be able to add bookmarks for podcasts, so letter I can listen again parts that I have bookmarked
3. I want to be able show the statics of my listening habits

## Frameworks

This is a pet project to play with:
* [FastAPI](https://fastapi.tiangolo.com/)
* [SqlAlchemy](https://www.sqlalchemy.org/)
* [Pydantic](https://pydantic-docs.helpmanual.io/)
* [Vue.js](https://vuejs.org/)
* [PrimeVue](https://www.primefaces.org/primevue/)
* [Spotify API](https://developer.spotify.com/documentation/web-api/)
* [Spotify Web Playback SDK](https://developer.spotify.com/documentation/web-playback-sdk/)
* eventually [GitHub Actions](https://github.com/features/actions)
* eventually [Azure](https://azure.microsoft.com/en-us/)

### Getting started

1. Clone the repository
3. Create a `.env` file in both `fastapi` and `vue` folders with the following content:
```
# fastapi/.env
SPOTIFY_CLIENT_ID="YOUR_SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET="YOUR_SPOTIFY_CLIENT_SECRET"

SECRET_KEY='YOUR_SECRET_KEY' # generate with openssl rand -hex 32
ALGORITHM='HS256'

ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_MINUTES=1440 # 24 hours

BASE_URL='http://localhost:8080'
BACKEND_URL='http://localhost:8000/api'
BACKEND_URL_DEBUG='http://localhost:8001/api'

POSTGRES_SERVER=postgres
POSTGRES_PORT=5432

POSTGRES_USER=YOUR_POSTGRES_USER
POSTGRES_PASSWORD='YOUR_POSTGRES_PASSWORD'
POSTGRES_DB=YOUR_POSTGRES_DB

# At the moment, the testing database is not used
POSTGRES_USER_TESTING=YOUR_POSTGRES_USER_TESTING
POSTGRES_PASSWORD_TESTING='YOUR_POSTGRES_PASSWORD_TESTING'
POSTGRES_DB_TESTING='YOUR_POSTGRES_DB_TESTING'
```

```
# vue/.env
VUE_APP_ENV=dev
VUE_APP_BASE_URL='http://localhost:8080'
VUE_APP_BACKEND_URL='http://localhost:8000/api'
VUE_APP_BACKEND_URL_DEBUG='http://localhost:8001/api'

VITE_ENV=dev
VITE_BASE_URL='http://localhost:8080'
VITE_BACKEND_URL='http://localhost:8000/api'
VITE_BACKEND_URL_DEBUG='http://localhost:8001/api'
```

2. Run `docker-compose up -d --build`
3. App should be available at `http://localhost:8080`

### APPs

#### 1 Spotify App

Just a simple Browser Spotify Player with simple interface. I try continuously to working on it. Altogether, it is a bit buggy, because I try here things out. Some buttons are not working.

Here is a screenshot of the current state:
![Spotify App](https://github.com/MijikHna/PLAYAREA3/blob/media/media/spotify-app.png?raw=true)

