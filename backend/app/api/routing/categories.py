from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from starlette.responses import Response

from app.schemas.categories import ProductCategoryScheme
from app.services.categories import ProductCategoryService


router = APIRouter(prefix="/products/categories", tags=["category"])


@router.get(
        "/{id}",
        status_code=status.HTTP_200_OK,
)
def get( 
    id: int, 
    productCategoryService: Annotated[ProductCategoryService, Depends()]
):
    return productCategoryService.get(id)


@router.get(
        "/", 
        status_code=status.HTTP_200_OK
)
def page(
    pageSize: int,
    startIndex: int,
    productCategoryService: Annotated[ProductCategoryService, Depends()]
):
    return productCategoryService.page(pageSize, startIndex)


@router.post(
    '/', 
    response_model=ProductCategoryScheme,
    status_code=status.HTTP_201_CREATED,
    )
def create(
    productCategory: ProductCategoryScheme,
    productCategoryService: Annotated[ProductCategoryService, Depends()]
) -> Response:
    return productCategoryService.create(productCategory)



