from pydantic import BaseModel


class ProductCategoryPostRequestScheme(BaseModel):
    name: str


class ProductCategoryScheme(ProductCategoryPostRequestScheme):
    id: int