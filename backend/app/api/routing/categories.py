from typing import Annotated
from fastapi import APIRouter, Depends, Query, status

from app.schemas.categories import ProductCategoryPostRequestScheme
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
    response_model=ProductCategoryPostRequestScheme,
    status_code=status.HTTP_201_CREATED
    )
def create(
    productCategory: ProductCategoryPostRequestScheme,
    productCategoryService: Annotated[ProductCategoryService, Depends()]
):
    return productCategoryService.create(productCategory)



