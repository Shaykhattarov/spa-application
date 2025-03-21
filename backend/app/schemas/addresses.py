from pydantic import BaseModel


class AddressesScheme(BaseModel):
    city: str
    street: str
    house: str
    apt: str


class AddressesUpdateScheme(AddressesScheme):
    id: int
