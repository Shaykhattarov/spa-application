from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from starlette.responses import Response, JSONResponse

from app.schemas.products import ProductScheme, ProductUpdateScheme
from app.services.products import ProductService


router = APIRouter(prefix="/products", tags=["Product"])


@router.post("/", response_model=ProductScheme, status_code=status.HTTP_201_CREATED)
def create_product(
    productScheme: ProductScheme, productService: Annotated[ProductService, Depends()]
) -> Response:
    return productService.create(productScheme)


@router.get("/", response_model=List[ProductScheme], status_code=status.HTTP_200_OK)
def read_products(
    productService: Annotated[ProductService, Depends()],
    skip: int = 0,
    limit: int = 100,
):
    return productService.page(skip, limit)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_product(id: int, productService: Annotated[ProductService, Depends()]):
    return productService.get(id)


@router.put(
    "/{id}",
    response_model=ProductUpdateScheme,
)
def put_product(
    productScheme: ProductUpdateScheme,
    productService: Annotated[ProductService, Depends()],
):
    return productService.put(productScheme)


@router.delete("/{id}")
def delete_product(id: int, productService: Annotated[ProductService, Depends()]):
    return productService.delete(id)
