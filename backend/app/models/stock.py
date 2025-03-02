from sqlmodel import SQLModel, Field
from decimal import Decimal
from typing import Optional



class Stock(SQLModel, table=True):
    __tablename__ = "stock"

    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="products.id", ondelete="RESTRICT")
    quantity: Decimal = Field(default=0, max_digits=10, decimal_places=3)
    
    



