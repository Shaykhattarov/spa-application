from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal


class Supply(SQLModel, table=True):
    __tablename__ = "supplies"

    id: int = Field(default=None, primary_key=True)

    store_id: Optional[int] = Field(default=None, foreign_key="stores.id", ondelete="RESTRICT")
    supplier_id: int | None = Field(default=None, foreign_key="suppliers.id", ondelete="RESTRICT")
    total_amount: Decimal = Field(default=0, max_digits=15, decimal_places=2)
    date: datetime