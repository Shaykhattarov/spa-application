from fastapi import Depends, status
from typing import Annotated, Optional, List
from fastapi.encoders import jsonable_encoder
from starlette.responses import Response, JSONResponse

from app.models.suppliers import Supplier
from app.schemas.suppliers import SupplierScheme, SupplierUpdateScheme
from app.repositories.suppliers import SupplierRepository


class SupplierService:
    supplierRepository: SupplierRepository

    def __init__(self, supplierRepository: SupplierRepository = Depends()):
        self.supplierRepository = supplierRepository

    def create(self, supplierScheme: SupplierScheme) -> Response:
        response: Optional[Supplier] = self.supplierRepository.create(
            Supplier(name=supplierScheme.name, category_id=supplierScheme.category_id)
        )

        if response is None:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={"location": f"/{Supplier.__tablename__}/{response.id}"},
        )

    def page(self, skip: int, limit: int) -> JSONResponse:
        response: List[Supplier] = self.supplierRepository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response,
        }
        return JSONResponse(content=jsonable_encoder(content))

    def get(self, id: int) -> Response | JSONResponse:
        response = self.supplierRepository.get(Supplier(id=id))
        if response is None:
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        else:
            return JSONResponse(
                status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
            )

    def put(self, productScheme: SupplierUpdateScheme) -> Response:
        response: Optional[Supplier] = self.supplierRepository.put(
            Supplier(
                id=productScheme.id,
                name=productScheme.name,
                category_id=productScheme.category_id,
            )
        )

        if response is None:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    def delete(self, id: int):
        self.supplierRepository.delete(id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
