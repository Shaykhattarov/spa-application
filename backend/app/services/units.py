from fastapi import Depends, status
from fastapi.encoders import jsonable_encoder
from typing import List
from starlette.responses import Response, JSONResponse

from app.repositories.units import ProductUnitRepository
from app.schemas.units import ProductUnitScheme
from app.models.units import ProductUnit



class ProductUnitService:

    productUnitRepository: ProductUnitRepository

    def __init__(self, productUnitRepository: ProductUnitRepository = Depends()) -> None:
        self.productUnitRepository = productUnitRepository

    def create(self, productUnitScheme: ProductUnitScheme) -> Response:
        new_obj: ProductUnit | None = self.productUnitRepository.create(ProductUnit(name=productUnitScheme.name))
        if new_obj is not None:
            return Response(
                status_code=status.HTTP_201_CREATED, 
                headers={
                    "location": f"/{ProductUnit.__tablename__}/{new_obj.id}"
                }
            )
        else:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def get(self, id: int) -> ProductUnit:
        response = self.productUnitRepository.get(
            ProductUnit(id=id)
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
    ) -> List[ProductUnit]:
        response: List[ProductUnit] = self.productUnitRepository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response
        }
        return JSONResponse(
            content=jsonable_encoder(content)
        )