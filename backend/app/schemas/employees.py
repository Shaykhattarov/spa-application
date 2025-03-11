from pydantic import BaseModel, Field
from typing import Annotated



class EmployeeScheme(BaseModel):
    name: str
    surname: str
    patronymic: str
    old: Annotated[
        int, 
        Field(default=0, max_digits=3)
    ]
    phone: str
    email: str
    store_id: int
    position_id: int


class EmployeeUpdateScheme(EmployeeScheme):
    id: int

