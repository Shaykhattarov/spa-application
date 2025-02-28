from typing import Annotated, List
from fastapi import APIRouter, Depends, status

from app.schemas.units import ProductUnitScheme
from app.services.units import ProductUnitService


router = APIRouter(prefix="/products/units", tags=["unit"])



@router.post(
    "/",
    response_model=ProductUnitScheme,
    status_code=status.HTTP_201_CREATED
)
def create_unit(
    productUnitScheme: ProductUnitScheme,
    productUnitService: Annotated[ProductUnitService, Depends()]
):
    return productUnitService.create(productUnitScheme)


@router.get(
    "/",
    response_model=List[ProductUnitScheme],
    status_code=status.HTTP_200_OK
)
def read_units(
    productUnitService: Annotated[ProductUnitService, Depends()],
    skip: int = 0,
    limit: int = 100,
):
    return productUnitService.page(skip, limit)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK
)
def get_unit(
    id: int,
    productCategoryService: Annotated[ProductUnitService, Depends()]
):
    return productCategoryService.get(id)
