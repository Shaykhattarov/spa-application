from sqlmodel import SQLModel, Field
from typing import Optional, Annotated


class Administrator(SQLModel, table=True):
    __tablename__ = "administrators"

    id: Annotated[int, Field(default=None, primary_key=True)]

    name: str
    surname: str

    password: Annotated[str, Field(min_length=8, max_length=2056)]
