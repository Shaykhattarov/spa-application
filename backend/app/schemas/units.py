from pydantic import BaseModel


class ProductUnitPostRequestScheme(BaseModel):
    name: str
    abbreviation: str 


class ProductUnitScheme(ProductUnitPostRequestScheme):
    id: int