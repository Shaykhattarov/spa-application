from sqlmodel import Field, SQLModel
from decimal import Decimal


class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: int = Field(default=None, primary_key=True)
    name: str

    category_id: int | None = Field(default=None, foreign_key="categories.id", ondelete="RESTRICT")
    unit_id: int | None = Field(default=None, foreign_key="units.id", ondelete="RESTRICT")

    value: Decimal = Field(default=0, max_digits=7, decimal_places=3)

    retail_price: Decimal = Field(default=0, max_digits=7, decimal_places=2)

