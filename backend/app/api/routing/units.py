from typing import Annotated
from fastapi import APIRouter, Depends, status

from app.schemas.units import ProductUnitPostRequestScheme
from app.services.units import ProductUnitService


router = APIRouter(prefix="/products/units", tags=["unit"])


@router.get(
        "/{id}",
        status_code=status.HTTP_200_OK,
)
def get( 
    id: int, 
    productUnitService: Annotated[ProductUnitService, Depends()]
):
    return productUnitService.get(id)


@router.get(
        "/", 
        status_code=status.HTTP_200_OK
)
def page(
    pageSize: int,
    startIndex: int,
    productUnitService: Annotated[ProductUnitService, Depends()]
):
    return productUnitService.page(pageSize, startIndex)



@router.post(
    '/', 
    response_model=ProductUnitPostRequestScheme,
    status_code=status.HTTP_201_CREATED
    )
def create(
    productUnit: ProductUnitPostRequestScheme,
    productUnitService: Annotated[ProductUnitService, Depends()]
):
    return productUnitService.create(productUnit)
