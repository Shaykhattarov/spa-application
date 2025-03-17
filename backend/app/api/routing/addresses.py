from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from starlette.responses import Response

from app.schemas.addresses import AddressesScheme, AddressesUpdateScheme
from app.services.addresses import AddressesService


router = APIRouter(prefix="/addresses", tags=["Address"])


@router.post("/", response_model=AddressesScheme, status_code=status.HTTP_201_CREATED)
def create_address(
    addressScheme: AddressesScheme,
    productService: Annotated[AddressesService, Depends()],
) -> Response:
    return productService.create(addressScheme)


@router.get("/", response_model=List[AddressesScheme], status_code=status.HTTP_200_OK)
def read_addresses(
    addressesService: Annotated[AddressesService, Depends()],
    skip: int = 0,
    limit: int = 100,
):
    return addressesService.page(skip, limit)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_address(id: int, addressService: Annotated[AddressesService, Depends()]):
    return addressService.get(id)


@router.put(
    "/{id}",
    response_model=AddressesUpdateScheme,
)
def put_address(
    addressScheme: AddressesUpdateScheme,
    addressService: Annotated[AddressesService, Depends()],
):
    return addressService.put(addressScheme)


@router.delete("/{id}")
def delete_address(id: int, addressService: Annotated[AddressesService, Depends()]):
    return addressService.delete(id)
