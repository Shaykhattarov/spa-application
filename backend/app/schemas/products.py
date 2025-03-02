from pydantic import BaseModel, Field
from typing import Annotated
from decimal import Decimal



class ProductScheme(BaseModel):
    name: Annotated[
        str, 
        Field(
            min_length=2, 
            max_length=120, 
            description="Название товара должно быть от 2 до 120 символов")
    ]
    category_id: int
    unit_id: int
    retail_price: Annotated[
        Decimal, 
        Field(
            default=0,
            max_digits=7,
            description="Розничная цена товара должна быть длиною до 7 цифр"
        )
    ]

