from typing import List, Optional
from fastapi import Depends, status
from fastapi.encoders import jsonable_encoder
from starlette.responses import Response, JSONResponse

from app.models.stores import Store
from app.repositories.stores import StoreRepository
from app.schemas.stores import StoreScheme, StoreUpdateScheme


class StoreService:
    repository: StoreRepository

    def __init__(self, repos: StoreRepository = Depends()):
        self.repository = repos

    def create(self, storeScheme: StoreScheme) -> Response:
        response: Optional[Store] = self.repository.create(
            Store(
                name=storeScheme.name,
                address_id=storeScheme.address_id,
                schedule_id=storeScheme.schedule_id,
                scheme=storeScheme.scheme,
            )
        )

        if response is None:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={"location": f"/{Store.__tablename__}/{response.id}"},
        )

    def get(self, id: int) -> Response | JSONResponse:
        response = self.repository.get(Store(id=id))
        if response is None:
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        else:
            return JSONResponse(
                status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
            )

    def page(self, skip: int, limit: int) -> JSONResponse:
        response: List[Store] = self.repository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response,
        }
        return JSONResponse(content=jsonable_encoder(content))

    def put(self, storeScheme: StoreUpdateScheme) -> Response:
        response: Optional[Store] = self.repository.put(
            Store(
                id=storeScheme.id,
                name=storeScheme.name,
                address_id=storeScheme.address_id,
                schedule_id=storeScheme.schedule_id,
                scheme=storeScheme.scheme,
            )
        )

        if response is None:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    def delete(self, id: int):
        self.repository.delete(id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
