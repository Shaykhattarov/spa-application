from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from starlette.responses import Response, JSONResponse

from app.schemas.products import ProductScheme
from app.services.products import ProductService



router = APIRouter(prefix='/products', tags=['product'])



@router.post(
        '/', 
        response_model=ProductScheme,
        status_code=status.HTTP_201_CREATED
)
def create_product(
    productScheme: ProductScheme,
    productService: Annotated[ProductService, Depends()]
) -> Response:
    return productService.create(productScheme)



@router.get(
    "/",
    response_model=List[ProductScheme],
    status_code=status.HTTP_200_OK
)
def read_products(
    productCategoryService: Annotated[ProductService, Depends()],
    skip: int = 0,
    limit: int = 100,
):
    return productCategoryService.page(skip, limit)



@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK
)
def get_category(
    id: int,
    productCategoryService: Annotated[ProductService, Depends()]
):
    return productCategoryService.get(id)