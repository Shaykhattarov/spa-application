from pydantic import BaseModel, Field
from typing import Annotated
from decimal import Decimal


class SupplySurchargeScheme(BaseModel):
    name: str
    supply_id: int
    amount: Annotated[Decimal, Field(default=0, max_digits=7, decimal_places=2)]


class SupplySurchargeUpdateScheme(SupplySurchargeScheme):
    id: int
