from typing import List
from fastapi import APIRouter, status, Depends, UploadFile, HTTPException

from sqlalchemy.orm import Session
from api.logic.dto.sheet_dto import TableCreateDto, TableDto, TableInfoDto
from api.logic.dto.user_dto import UserBaseDto
from api.logic.services.sheet_service import SheetService

from api.logic.utils.auth import get_user_from_token
from api.logic.utils.db_manager import open_db_session

sheet_router: APIRouter = APIRouter(
    prefix='/api/sheet',
    tags=['sheet']
)


@sheet_router.post(
    '/create',
    response_model=TableDto,
    status_code=status.HTTP_201_CREATED
)
async def create_table(
    table: TableCreateDto,
    user: UserBaseDto = Depends(get_user_from_token),
    sheet_srv: SheetService = Depends(SheetService),
    db_session: Session = Depends(open_db_session)
) -> TableDto:
    return sheet_srv.create_table(db_session, table, user)


@sheet_router.get(
    '/tables',
    response_model=List[TableInfoDto],
    status_code=status.HTTP_200_OK
)
async def get_user_tables(
    user: UserBaseDto = Depends(get_user_from_token),
    sheet_srv: SheetService = Depends(SheetService),
    db_session: Session = Depends(open_db_session)
) -> List[TableInfoDto]:
    return sheet_srv.get_user_tables(db_session, user)


@sheet_router.get(
    '/tables/{id}',
    response_model=TableDto,
    status_code=status.HTTP_200_OK
)
async def get_table(
    id: int,
    user: UserBaseDto = Depends(get_user_from_token),
    sheet_srv: SheetService = Depends(SheetService),
    db_session: Session = Depends(open_db_session)
) -> TableDto:
    return sheet_srv.get_user_table(db_session, id, user)
