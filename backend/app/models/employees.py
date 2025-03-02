from sqlmodel import SQLModel, Field
from typing import Optional


class Employee(SQLModel, table=True):
    __tablename__ = "employees"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    surname: str
    patronymic: str
    old: int = Field(default=0, max_digits=3)
    phone: str
    email: str
    store_id: Optional[int] = Field(default=None, foreign_key="stores.id", ondelete="RESTRICT")
    position_id: Optional[int] = Field(default=None, foreign_key="employee_positions.id", ondelete="RESTRICT")