from pydantic import BaseModel


class ProductUnitPostRequestScheme(BaseModel):
    name: str


class ProductUnitScheme(ProductUnitPostRequestScheme):
    id: int