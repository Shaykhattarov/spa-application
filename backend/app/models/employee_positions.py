from sqlmodel import SQLModel, Field
from typing import Optional



class EmployeePosition(SQLModel, table=True):
    __tablename__ = "employee_positions"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str