from pydantic import BaseModel, Field
from typing import Annotated
from decimal import Decimal


class StoreScheme(BaseModel):
    name: str
    address_id: int
    schedule_id: int
    scheme: str


class StoreUpdateScheme(StoreScheme):
    id: int
