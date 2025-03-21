from typing import Annotated

from fastapi import APIRouter, Depends, status
from starlette.responses import Response

from app.services.suppliers import SupplierService
from app.schemas.suppliers import SupplierScheme, SupplierUpdateScheme


router = APIRouter(prefix="/suppliers", tags=["Supplier"])


@router.post("/", response_model=SupplierScheme, status_code=status.HTTP_201_CREATED)
def create_supplier(
    supplierScheme: SupplierScheme,
    supplierService: Annotated[SupplierService, Depends()],
) -> Response:
    return supplierService.create(supplierScheme)


@router.get("/")
def read_suppliers(
    supplierService: Annotated[SupplierService, Depends()],
    skip: int = 0,
    limit: int = 100,
) -> Response:
    return supplierService.page(skip, limit)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_supplier(
    supplierService: Annotated[SupplierService, Depends()], id: int
) -> Response:
    return supplierService.get(id)


@router.put(
    "/{id}",
    response_model=SupplierUpdateScheme,
)
def put_product(
    productScheme: SupplierUpdateScheme,
    productService: Annotated[SupplierService, Depends()],
) -> Response:
    return productService.put(productScheme)


@router.delete("/{id}")
def delete_product(
    id: int, productService: Annotated[SupplierService, Depends()]
) -> Response:
    return productService.delete(id)
