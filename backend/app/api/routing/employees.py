from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from starlette.responses import Response

from app.schemas.employees import EmployeeScheme, EmployeeUpdateScheme
from app.services.employees import EmployeeService


router = APIRouter(prefix="/employees", tags=["Employee"])


@router.post("/", response_model=EmployeeScheme, status_code=status.HTTP_201_CREATED)
def create_employee(
    employeeScheme: EmployeeScheme,
    employeeService: Annotated[EmployeeService, Depends()],
) -> Response:
    return employeeService.create(employeeScheme)


@router.get("/", response_model=List[EmployeeScheme], status_code=status.HTTP_200_OK)
def read_employees(
    employeeService: Annotated[EmployeeService, Depends()],
    skip: int = 0,
    limit: int = 100,
):
    return employeeService.page(skip, limit)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_employee(id: int, employeeService: Annotated[EmployeeService, Depends()]):
    return employeeService.get(id)


@router.put(
    "/{id}",
    response_model=EmployeeUpdateScheme,
)
def put_employee(
    employeeScheme: EmployeeUpdateScheme,
    employeeService: Annotated[EmployeeService, Depends()],
):
    return employeeService.put(employeeScheme)


@router.delete("/{id}")
def delete_employee(id: int, employeeService: Annotated[EmployeeService, Depends()]):
    return employeeService.delete(id)
