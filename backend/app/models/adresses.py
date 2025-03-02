from sqlmodel import SQLModel, Field
from typing import Optional


class Addresses(SQLModel, table=True):
    __tablename__ = "addresses"

    id: Optional[int] = Field(default=None, primary_key=True)
    city: str
    street: str
    house: str
    apt: str