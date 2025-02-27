from pydantic import BaseModel, Field
from typing import Annotated


class ProductCategoryScheme(BaseModel):
    name: Annotated[
        str, 
        Field(min_length=2, max_length=60, description="Название категории должно быть от 2 до 60 символов")
    ]


