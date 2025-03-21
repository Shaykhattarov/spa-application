from pydantic import BaseModel


class StoreScheduleScheme(BaseModel):
    day_of_week: str
    open_time: str
    close_time: str


class StoreScheduleUpdateScheme(StoreScheduleScheme):
    id: int
