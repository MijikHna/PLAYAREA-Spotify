from fastapi import APIRouter,  status
from fastapi.responses import JSONResponse

base_router: APIRouter = APIRouter(
    prefix='',
    tags=['base']
)


@base_router.get(
    '/',
)
async def get_base() -> JSONResponse:
    return JSONResponse(
        content={'message': 'OK'},
        status_code=status.HTTP_200_OK
    )
