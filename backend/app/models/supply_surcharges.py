from sqlmodel import SQLModel, Field
from decimal import Decimal



class SupplySurcharge(SQLModel, table=True):
    __tablename__ = "supply_surcharges"

    id: int = Field(default=None, primary_key=True)
    supply_id: int = Field(default=None, foreign_key="supplies.id", ondelete="RESTRICT")
    name: str
    amount: Decimal = Field(default=0, max_digits=7, decimal_places=2)