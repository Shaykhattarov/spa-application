from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: int = Field(default=None, primary_key=True)
    name: str

    category_id: int | None = Field(default=None, foreign_key="categories.id", ondelete="RESTRICT")
    unit_id: int | None = Field(default=None, foreign_key="units.id", ondelete="RESTRICT")

    retail_price: int

