from fastapi import Depends, status
from typing import Annotated, Optional, List
from fastapi.encoders import jsonable_encoder
from starlette.responses import Response, JSONResponse

from app.models.supplies import Supply
from app.repositories.supplies import SupplyRepository
from app.schemas.supplies import SupplyScheme, SupplyUpdateScheme


class SupplyService:
    repository: SupplyRepository

    def __init__(self, repo: Annotated[SupplyRepository, Depends()]):
        self.repository = repo

    def create(self, supplyScheme: SupplyScheme) -> Response:
        response: Optional[Supply] = self.repository.create(
            Supply(
                date=supplyScheme.date,
                store_id=supplyScheme.store_id,
                supplier_id=supplyScheme.supplier_id,
                total_amount=supplyScheme.total_amount,
            )
        )

        if response is None:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={"location": f"/{Supply.__tablename__}/{response.id}"},
        )

    def get(self, id: int) -> Response | JSONResponse:
        response = self.repository.get(Supply(id=id))
        if response is None:
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        else:
            return JSONResponse(
                status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
            )

    def page(self, skip: int, limit: int) -> JSONResponse:
        response: List[Supply] = self.repository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response,
        }
        return JSONResponse(content=jsonable_encoder(content))

    def put(self, supplyScheme: SupplyUpdateScheme) -> Response:
        response: Optional[Supply] = self.repository.put(
            Supply(
                id=supplyScheme.id,
                date=supplyScheme.date,
                store_id=supplyScheme.store_id,
                supplier_id=supplyScheme.supplier_id,
                total_amount=supplyScheme.total_amount,
            )
        )

        if response is None:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    def delete(self, id: int):
        self.repository.delete(id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
