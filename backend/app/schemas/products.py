from pydantic import BaseModel
from decimal import Decimal



class ProductScheme(BaseModel):
    name: str
    category_id: int
    unit_id: str
    retail_price: Decimal


class ProductCategoryScheme(BaseModel):
    name: str


class ProductUnitScheme(BaseModel):
    name: str