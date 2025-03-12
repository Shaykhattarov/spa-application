from fastapi import Depends, status
from typing import Annotated, Optional, List
from fastapi.encoders import jsonable_encoder
from starlette.responses import Response, JSONResponse

from app.models.employee_positions import EmployeePosition
from app.schemas.employee_positions import EmployeePositionScheme, EmployeePositionUpdateScheme
from app.repositories.employee_positions import EmployeePositionRepository


class EmployeeService:

    repository: EmployeePositionRepository

    def __init__(self, repo: EmployeePositionRepository = Depends()):
        self.repository = repo

    def create(self, employeePositionScheme: EmployeePositionScheme) -> Response:
        response: Optional[EmployeePosition] = self.repository.create(
            EmployeePosition(
                name=employeePositionScheme.name
            )
        )

        if response is None:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={
                "location": f"/{EmployeePosition.__tablename__}/{response.id}" 
            }
        )
        

    def get(self, id: int) -> Response | JSONResponse:
        response = self.repository.get(
            EmployeePosition(id=id)
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
        response: List[EmployeePosition] = self.repository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response
        }
        return JSONResponse(
            content=jsonable_encoder(content)
        )

    def put(self, employeeScheme: EmployeePositionUpdateScheme) -> Response:
        response: Optional[EmployeePosition] = self.repository.put(
            EmployeePosition(
                id=employeeScheme.id,
                name=employeeScheme.name,
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

    