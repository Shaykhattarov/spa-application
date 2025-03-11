from pydantic import BaseModel, Field
from typing import Annotated



class AddressesScheme(BaseModel):
    city: str
    street: str
    house: str
    apt: str


class AddressesUpdateScheme(AddressesScheme):
    id: int

