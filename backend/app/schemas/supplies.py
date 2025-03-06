from pydantic import BaseModel, Field
from typing import Annotated
from decimal import Decimal
from datetime import datetime



class SupplyScheme(BaseModel):
    store_id: int
    supplier_id: int
    total_amount: Annotated[
        Decimal,
        Field(
            default=0,
            max_digits=15, 
            decimal_places=2
        )
    ]
    date: datetime



class SupplyUpdateScheme(SupplyScheme):
    id: int
    
