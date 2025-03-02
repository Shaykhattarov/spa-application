from sqlmodel import SQLModel, Field
from decimal import Decimal



class SupplyItem(SQLModel, table=True):
    __tablename__ = "supply_items"

    id: int = Field(default=None, primary_key=True)
    supply_id: int | None = Field(default=None, foreign_key="supplies.id", ondelete="RESTRICT")
    product_id: int | None = Field(default=None, foreign_key="products.id")
    quantity: int
    price: Decimal = Field(default=0, max_digits=7, decimal_places=2)