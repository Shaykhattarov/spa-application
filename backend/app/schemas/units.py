from pydantic import BaseModel, Field
from typing import Annotated


class ProductUnitScheme(BaseModel):
    name: Annotated[
        str, 
        Field(
            min_length=2, 
            max_length=30, 
            description="Название ед. имзерения должно быть от 2 до 30 символов"
        )
    ]
    
    abbreviation: Annotated[
        str,
        Field(
            min_length=2,
            max_length=10,
            description="Аббревиатура ед. измерения должна быть от 2 до 10 символов"
        )
    ]