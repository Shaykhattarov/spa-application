from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from starlette.responses import Response, JSONResponse

from app.services.supply_items import SupplyItemService
from app.schemas.supply_items import SupplyItemScheme, SupplyItemUpdateScheme



router = APIRouter(prefix="/supplies/items", tags=["Supply Item"])


@router.post(
    "/",
    response_model=SupplyItemScheme
)
def create_supply_item(
    scheme: SupplyItemScheme,
    service: Annotated[SupplyItemService, Depends()]
):
    return service.create(scheme)


@router.get(
    "/",
    response_model=List[SupplyItemScheme],
    status_code=status.HTTP_200_OK
)
def read_supply_items(
    service: Annotated[SupplyItemService, Depends()],
    skip: int = 0,
    limit: int = 100,
):
    return service.page(skip, limit)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK
)
def get_supply_item(
    id: int, 
    service: Annotated[SupplyItemService, Depends()]
):
    return service.get(id)


@router.put(
    "/{id}",
    response_model=SupplyItemUpdateScheme,
)
def put_product(
    scheme: SupplyItemUpdateScheme,
    service: Annotated[SupplyItemService, Depends()]
):
    return service.put(scheme)


@router.delete(
    "/{id}"
)
def delete_product(
    id: int,
    service: Annotated[SupplyItemService, Depends()]
):
    return service.delete(id)