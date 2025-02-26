from sqlmodel import Field, SQLModel



class ProductCategory(SQLModel, table=True):
    __tablename__ = "categories"

    id: int = Field(default=None, primary_key=True)
    name: str 