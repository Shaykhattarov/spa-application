from sqlmodel import SQLModel, Field
from typing import Optional



class Store(SQLModel, table=True):
    __tablename__ = "stores"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address_id: Optional[int] = Field(default=None, foreign_key="addresses.id", ondelete="RESTRICT")
    schedule_id: Optional[int] = Field(default=None, foreign_key="store_schedules.id", ondelete="RESTRICT")
    scheme: str