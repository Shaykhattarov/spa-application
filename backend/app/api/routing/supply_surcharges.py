from typing import Annotated, List
from fastapi import APIRouter, Depends, status

from app.services.supply_surcharges import SupplySurchargeService
from app.schemas.supply_surcharges import SupplySurchargeScheme, SupplySurchargeUpdateScheme


router = APIRouter(prefix="/supply_surcharges", tags=["supply_surcharge"])


@router.post(
    "/",
    response_model=SupplySurchargeScheme
)
def create_supply_item(
    scheme: SupplySurchargeScheme,
    service: Annotated[SupplySurchargeService, Depends()]
):
    return service.create(scheme)


@router.get(
    "/",
    response_model=List[SupplySurchargeScheme],
    status_code=status.HTTP_200_OK
)
def read_supply_items(
    service: Annotated[SupplySurchargeService, Depends()],
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
    service: Annotated[SupplySurchargeService, Depends()]
):
    return service.get(id)


@router.put(
    "/{id}",
    response_model=SupplySurchargeUpdateScheme,
)
def put_product(
    scheme: SupplySurchargeUpdateScheme,
    service: Annotated[SupplySurchargeService, Depends()]
):
    return service.put(scheme)


@router.delete(
    "/{id}"
)
def delete_product(
    id: int,
    service: Annotated[SupplySurchargeService, Depends()]
):
    return service.delete(id)