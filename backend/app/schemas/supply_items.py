from pydantic import BaseModel, Field
from typing import Annotated
from decimal import Decimal



class SupplyItemScheme(BaseModel):
    supply_id: int
    product_id: int
    quantity: int
    price: Annotated[
        Decimal, 
        Field(
            default=0,
            max_digits=7,
            decimal_places=2
        )
    ]


class SupplyItemUpdateScheme(SupplyItemScheme):
    id: int
