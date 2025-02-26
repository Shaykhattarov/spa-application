from pydantic import BaseModel



class ProductScheme(BaseModel):
    name: str


class ProductCategoryScheme(BaseModel):
    name: str


class ProductUnitScheme(BaseModel):
    name: str