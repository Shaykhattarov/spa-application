from fastapi import Depends, status
from typing import Annotated, Optional, List
from fastapi.encoders import jsonable_encoder
from starlette.responses import Response, JSONResponse

from app.models.store_schedules import StoreSchedule
from app.schemas.store_schedules import StoreScheduleScheme, StoreScheduleUpdateScheme
from app.repositories.store_schedules import StoreScheduleRepository


class StoreScheduleService:
    repository: StoreScheduleRepository

    def __init__(self, repo: StoreScheduleRepository = Depends()):
        self.repository = repo

    def create(self, storeScheduleScheme: StoreScheduleScheme) -> Response:
        response: Optional[StoreSchedule] = self.repository.create(
            StoreSchedule(
                day_of_week=storeScheduleScheme.day_of_week,
                open_time=storeScheduleScheme.open_time,
                close_time=storeScheduleScheme.close_time,
            )
        )

        if response is None:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={"location": f"/{StoreSchedule.__tablename__}/{response.id}"},
        )

    def get(self, id: int) -> Response | JSONResponse:
        response = self.repository.get(StoreSchedule(id=id))
        if response is None:
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        else:
            return JSONResponse(
                status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
            )

    def page(self, skip: int, limit: int) -> JSONResponse:
        response: List[StoreSchedule] = self.repository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response,
        }
        return JSONResponse(content=jsonable_encoder(content))

    def put(self, storeScheduleScheme: StoreScheduleUpdateScheme) -> Response:
        response: Optional[StoreSchedule] = self.repository.put(
            StoreSchedule(
                id=storeScheduleScheme.id,
                day_of_week=storeScheduleScheme.day_of_week,
                open_time=storeScheduleScheme.open_time,
                close_time=storeScheduleScheme.close_time,
            )
        )

        if response is None:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    def delete(self, id: int):
        self.repository.delete(id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
