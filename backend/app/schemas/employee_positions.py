from pydantic import BaseModel


class EmployeePositionScheme(BaseModel):
    name: str


class EmployeePositionUpdateScheme(EmployeePositionScheme):
    id: int
