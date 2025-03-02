from sqlmodel import SQLModel, Field




class Supplier(SQLModel, table=True):
    __tablename__ = "suppliers"

    id: int = Field(default=None, primary_key=True)
    name: str = Field()

    category_id: int | None = Field(default=None, foreign_key="categories.id", ondelete="RESTRICT")