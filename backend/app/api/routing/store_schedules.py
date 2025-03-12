from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from starlette.responses import Response

from app.schemas.store_schedules import StoreScheduleScheme, StoreScheduleUpdateScheme
from app.services.store_schedules import StoreScheduleService



router = APIRouter(prefix='/stores/schedules', tags=['Store Schedule'])



@router.post(
        '/', 
        response_model=StoreScheduleScheme,
        status_code=status.HTTP_201_CREATED
)
def create_store_schedule(
    storeScheduleScheme: StoreScheduleScheme,
    productService: Annotated[StoreScheduleService, Depends()]
) -> Response:
    return productService.create(storeScheduleScheme)



@router.get(
    "/",
    response_model=List[StoreScheduleScheme],
    status_code=status.HTTP_200_OK
)
def read_store_schedules(
    storeScheduleService: Annotated[StoreScheduleService, Depends()],
    skip: int = 0,
    limit: int = 100,
):
    return storeScheduleService.page(skip, limit)



@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK
)
def get_store_schedule(
    id: int,
    storeScheduleService: Annotated[StoreScheduleService, Depends()]
):
    return storeScheduleService.get(id)


@router.put(
    "/{id}",
    response_model=StoreScheduleUpdateScheme,
)
def put_store_schedule(
    storeScheduleScheme: StoreScheduleUpdateScheme,
    storeScheduleService: Annotated[StoreScheduleService, Depends()]
):
    return storeScheduleService.put(storeScheduleScheme)


@router.delete(
    "/{id}"
)
def delete_store_schedule(
    id: int,
    storeScheduleService: Annotated[StoreScheduleService, Depends()]
):
    return storeScheduleService.delete(id)