from sqlmodel import SQLModel, Field
from typing import Optional

class StoreSchedule(SQLModel, table=True):
    __tablename__ = "store_schedules"

    id: Optional[int] = Field(default=None, primary_key=True)
    day_of_week: str
    open_time: str
    close_time: str