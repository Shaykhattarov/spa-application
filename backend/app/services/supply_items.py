from fastapi import Depends, status
from typing import Annotated, Optional, List
from fastapi.encoders import jsonable_encoder
from starlette.responses import Response, JSONResponse

from app.models.supply_items import SupplyItem
from app.schemas.supply_items import SupplyItemScheme, SupplyItemUpdateScheme
from app.repositories.supply_items import SupplyItemRepository


class SupplyItemService:

    repository: SupplyItemRepository

    def __init__(self, repo: SupplyItemRepository = Depends()):
        self.repository = repo

    def create(self, supplyItemScheme: SupplyItemScheme) -> Response:
        response: Optional[SupplyItem] = self.repository.create(
            SupplyItem(
                supply_id=supplyItemScheme.supply_id,
                product_id=supplyItemScheme.product_id,
                quantity=supplyItemScheme.quantity,
                price=supplyItemScheme.price,
            )
        )

        if response is None:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={
                "location": f"/{SupplyItem.__tablename__}/{response.id}" 
            }
        )
        

    def get(self, id: int) -> Response | JSONResponse:
        response = self.repository.get(
            SupplyItem(id=id)
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
        response: List[SupplyItem] = self.repository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response
        }
        return JSONResponse(
            content=jsonable_encoder(content)
        )

    def put(self, supplyItemUpdateScheme: SupplyItemUpdateScheme) -> Response:
        response: Optional[SupplyItem] = self.repository.put(
            SupplyItem(
                id=supplyItemUpdateScheme.id,
                supply_id=supplyItemUpdateScheme.supply_id,
                product_id=supplyItemUpdateScheme.product_id,
                quantity=supplyItemUpdateScheme.quantity,
                price=supplyItemUpdateScheme.price,
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

    