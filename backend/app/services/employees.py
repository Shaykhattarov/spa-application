from fastapi import Depends, status
from typing import Annotated, Optional, List
from fastapi.encoders import jsonable_encoder
from starlette.responses import Response, JSONResponse

from app.models.employees import Employee
from app.schemas.employees import EmployeeScheme, EmployeeUpdateScheme
from app.repositories.employees import EmployeeRepository


class EmployeeService:

    repository: EmployeeRepository

    def __init__(self, repo: EmployeeRepository = Depends()):
        self.repository = repo

    def create(self, employeeScheme: EmployeeScheme) -> Response:
        response: Optional[Employee] = self.repository.create(
            Employee(
                name=employeeScheme.name,
                surname = employeeScheme.surname,
                patronymic = employeeScheme.patronymic,
                old = employeeScheme.old,
                phone = employeeScheme.phone,
                email = employeeScheme.email,
                store_id = employeeScheme.store_id,
                position_id = employeeScheme.position_id,
            )
        )

        if response is None:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={
                "location": f"/{Employee.__tablename__}/{response.id}" 
            }
        )
        

    def get(self, id: int) -> Response | JSONResponse:
        response = self.repository.get(
            Employee(id=id)
        )
        if response is None:
            return Response(
                status_code=status.HTTP_404_NOT_FOUND
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(response)
            )
        
    def page(
            self,
            skip: int,
            limit: int
    ) -> JSONResponse:
        response: List[Employee] = self.repository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response
        }
        return JSONResponse(
            content=jsonable_encoder(content)
        )

    def put(self, employeeScheme: EmployeeUpdateScheme) -> Response:
        response: Optional[Employee] = self.repository.put(
            Employee(
                id=employeeScheme.id,
                name=employeeScheme.name,
                surname = employeeScheme.surname,
                patronymic = employeeScheme.patronymic,
                old = employeeScheme.old,
                phone = employeeScheme.phone,
                email = employeeScheme.email,
                store_id = employeeScheme.store_id,
                position_id = employeeScheme.position_id,
            )
        )

        if response is None:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        else:
            return Response(
                status_code=status.HTTP_204_NO_CONTENT
            )
        

    def delete(self, id: int):
        self.repository.delete(id)

        return Response(
            status_code=status.HTTP_204_NO_CONTENT
        )

    