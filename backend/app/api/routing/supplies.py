from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from starlette.responses import Response, JSONResponse

from app.services.supplies import SupplyService
from app.repositories.supplies import SupplyRepository
from app.schemas.supplies import SupplyScheme, SupplyUpdateScheme



router = APIRouter(prefix='/supplies', tags=['Supply'])



@router.post(
        '/', 
        response_model=SupplyScheme,
        status_code=status.HTTP_201_CREATED
)
def create_supply(
    supplyScheme: SupplyScheme,
    supplyService: Annotated[SupplyService, Depends()]
) -> Response:
    return supplyService.create(supplyScheme)



@router.get(
    "/",
    response_model=List[SupplyScheme],
    status_code=status.HTTP_200_OK
)
def read_supplies(
    supplyService: Annotated[SupplyService, Depends()],
    skip: int = 0,
    limit: int = 100,
):
    return supplyService.page(skip, limit)



@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK
)
def get_supply(
    id: int,
    supplyService: Annotated[SupplyService, Depends()]
):
    return supplyService.get(id)


@router.put(
    "/{id}",
    response_model=SupplyUpdateScheme,
)
def put_supply(
    supplyScheme: SupplyUpdateScheme,
    supplyService: Annotated[SupplyService, Depends()]
):
    return supplyService.put(supplyScheme)


@router.delete(
    "/{id}"
)
def delete_supply(
    id: int,
    supplyService: Annotated[SupplyService, Depends()]
):
    return supplyService.delete(id)