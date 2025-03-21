from fastapi import Depends, status
from typing import Optional, List
from fastapi.encoders import jsonable_encoder
from starlette.responses import Response, JSONResponse

from app.models.addresses import Addresses
from app.schemas.addresses import AddressesScheme, AddressesUpdateScheme
from app.repositories.addresses import AddressesRepository


class AddressesService:
    repository: AddressesRepository

    def __init__(self, repo: AddressesRepository = Depends()):
        self.repository = repo

    def create(self, addressScheme: AddressesScheme) -> Response:
        response: Optional[Addresses] = self.repository.create(
            Addresses(
                city=addressScheme.city,
                street=addressScheme.street,
                house=addressScheme.house,
                apt=addressScheme.apt,
            )
        )

        if response is None:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={"location": f"/{Addresses.__tablename__}/{response.id}"},
        )

    def get(self, id: int) -> Response | JSONResponse:
        response = self.repository.get(Addresses(id=id))
        if response is None:
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        else:
            return JSONResponse(
                status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
            )

    def page(self, skip: int, limit: int) -> JSONResponse:
        response: List[Addresses] = self.repository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response,
        }
        return JSONResponse(content=jsonable_encoder(content))

    def put(self, addressUpdateScheme: AddressesUpdateScheme) -> Response:
        response: Optional[Addresses] = self.repository.put(
            Addresses(
                id=addressUpdateScheme.id,
                city=addressUpdateScheme.city,
                street=addressUpdateScheme.street,
                house=addressUpdateScheme.house,
                apt=addressUpdateScheme.apt,
            )
        )

        if response is None:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    def delete(self, id: int):
        self.repository.delete(id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
