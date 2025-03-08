from fastapi import Depends, status
from typing import Optional, List
from fastapi.encoders import jsonable_encoder
from starlette.responses import Response, JSONResponse

from app.models.supply_surcharges import SupplySurcharge
from app.repositories.supply_surcharges import SupplySurchargeRepository
from app.schemas.supply_surcharges import SupplySurchargeScheme, SupplySurchargeUpdateScheme



class SupplySurchargeService:

    repository: SupplySurchargeRepository

    def __init__(self, repo: SupplySurchargeRepository = Depends()):
        self.repository = repo

    def create(self, scheme: SupplySurchargeScheme) -> Response:
        response: Optional[SupplySurcharge] = self.repository.create(
            SupplySurcharge(
                name=scheme.name,
                supply_id=scheme.supply_id,
                amount=scheme.amount,
            )
        )

        if response is None:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={
                "location": f"/{SupplySurcharge.__tablename__}/{response.id}" 
            }
        ) 
    
    def get(self, id: int) -> Response:
        response = self.repository.get(
            SupplySurcharge(id=id)
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
        response: List[SupplySurcharge] = self.repository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response
        }
        return JSONResponse(
            content=jsonable_encoder(content)
        )
    
    def put(self, scheme: SupplySurchargeUpdateScheme) -> Response:
        response: Optional[SupplySurcharge] = self.repository.put(
            SupplySurcharge(
                id=scheme.id,
                name=scheme.name,
                supply_id=scheme.supply_id,
                amount=scheme.amount
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
    