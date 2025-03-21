from typing import Annotated, List
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.dependencies import CurrentAdministrator
from app.schemas.administrators import AdministratorScheme, AdministratorAuthScheme
from app.services.administrators import AdministratorService


router = APIRouter(prefix="/administrators", tags=["Administrator"])


@router.post("/login/access-token")
def login_administrator_for_access_token(
    serviceAdministrator: Annotated[AdministratorService, Depends()], 
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    return serviceAdministrator.authenticate(form_data)

@router.get(
        "/login/test-token", 
        response_model=AdministratorAuthScheme
)
def test_token(current_admin: CurrentAdministrator):
    return current_admin


@router.post(
    "/", 
    response_model=AdministratorScheme, 
    status_code=status.HTTP_201_CREATED
)
def create_administrator(
    adminScheme: AdministratorScheme,
    adminService: Annotated[AdministratorService, Depends()],
):
    return adminService.create(adminScheme)


@router.get(
    "/", response_model=List[AdministratorScheme], status_code=status.HTTP_200_OK
)
def read_administrators(
    adminService: Annotated[AdministratorService, Depends()],
    skip: int = 0,
    limit: int = 100,
):
    return adminService.page(skip, limit)


@router.put(
    "/{id}",
    response_model=AdministratorScheme,
)
def put_administrator(
    adminScheme: AdministratorScheme,
    adminService: Annotated[AdministratorService, Depends()],
):
    return adminService.put(adminScheme)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_administrator(
    id: int, adminService: Annotated[AdministratorService, Depends()]
):
    return adminService.get(id)


@router.delete("/{id}")
def delete_administrator(id: int, adminService: Annotated[AdministratorService, Depends()]):
    return adminService.delete(id)
