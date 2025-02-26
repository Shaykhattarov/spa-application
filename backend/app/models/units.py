from sqlmodel import Field, SQLModel



class ProductUnit(SQLModel, table=True):
    __tablename__ = "units"

    id: int = Field(default=None, primary_key=True)
    name: str
    abbreviation: str 