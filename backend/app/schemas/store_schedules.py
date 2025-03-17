from pydantic import BaseModel, Field
from typing import Annotated


class StoreScheduleScheme(BaseModel):
    day_of_week: str
    open_time: str
    close_time: str


class StoreScheduleUpdateScheme(StoreScheduleScheme):
    id: int
