from pydantic import BaseModel, Field
from typing import Annotated


class EmployeePositionScheme(BaseModel):
    name: str


class EmployeePositionUpdateScheme(EmployeePositionScheme):
    id: int
