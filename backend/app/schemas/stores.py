from pydantic import BaseModel


class StoreScheme(BaseModel):
    name: str
    address_id: int
    schedule_id: int
    scheme: str


class StoreUpdateScheme(StoreScheme):
    id: int
