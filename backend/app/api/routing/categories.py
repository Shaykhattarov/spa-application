from typing import Annotated, List
from fastapi import APIRouter, Depends, status

from app.schemas.categories import ProductCategoryScheme
from app.services.categories import ProductCategoryService


router = APIRouter(prefix="/products/categories", tags=["Category"])


@router.post(
    "/", response_model=ProductCategoryScheme, status_code=status.HTTP_201_CREATED
)
def create_category(
    productCategoryScheme: ProductCategoryScheme,
    productCategoryService: Annotated[ProductCategoryService, Depends()],
):
    return productCategoryService.create(productCategoryScheme)


@router.get(
    "/", response_model=List[ProductCategoryScheme], status_code=status.HTTP_200_OK
)
def read_categories(
    productCategoryService: Annotated[ProductCategoryService, Depends()],
    skip: int = 0,
    limit: int = 100,
):
    return productCategoryService.page(skip, limit)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_category(
    id: int, productCategoryService: Annotated[ProductCategoryService, Depends()]
):
    return productCategoryService.get(id)


@router.delete("/{id}")
def delete_category(id: int, categoryService: ProductCategoryService):
    return ProductCategoryService.delete(id)
