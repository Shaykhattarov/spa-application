from sqlmodel import Field, SQLModel



class ProductUnit(SQLModel, table=True):
    __tablename__ = "units"

    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=30, min_length=2)
    abbreviation: str = Field(max_length=10, min_length=2)