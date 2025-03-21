from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from starlette.responses import Response

from app.schemas.stores import StoreScheme, StoreUpdateScheme
from app.services.stores import StoreService


router = APIRouter(prefix="/stores", tags=["Store"])


@router.post("/", response_model=StoreScheme, status_code=status.HTTP_201_CREATED)
def create_store(
    storeScheme: StoreScheme, storeService: Annotated[StoreService, Depends()]
) -> Response:
    return storeService.create(storeScheme)


@router.get("/", response_model=List[StoreScheme], status_code=status.HTTP_200_OK)
def read_stores(
    storeService: Annotated[StoreService, Depends()],
    skip: int = 0,
    limit: int = 100,
):
    return storeService.page(skip, limit)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_store(id: int, storeService: Annotated[StoreService, Depends()]):
    return storeService.get(id)


@router.put(
    "/{id}",
    response_model=StoreUpdateScheme,
)
def put_store(
    storeScheme: StoreUpdateScheme, storeService: Annotated[StoreService, Depends()]
):
    return storeService.put(storeScheme)


@router.delete("/{id}")
def delete_store(id: int, storeService: Annotated[StoreService, Depends()]):
    return storeService.delete(id)
