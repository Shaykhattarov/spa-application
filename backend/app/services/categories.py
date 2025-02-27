from fastapi import Depends, status
from typing import Optional, List
from starlette.responses import Response

from app.models.categories import ProductCategory
from app.repositories.categories import ProductCategoryRepository
from app.schemas.categories import ProductCategoryScheme



class ProductCategoryService:

    productCategoryRepository: ProductCategoryRepository

    def __init__(self, productCategoryRepository: ProductCategoryRepository = Depends()) -> None:
        self.productCategoryRepository = productCategoryRepository

    def create(self, category: ProductCategoryScheme) -> Response:
        new_obj: ProductCategory | None = self.productCategoryRepository.create(ProductCategory(name=category.name))
        if new_obj is not None:
            return Response(
                status_code=status.HTTP_201_CREATED, 
                headers={
                    "location": f"/{ProductCategory.__tablename__}/{new_obj.id}"
                }
            )
        else:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def get(self, id: int) -> ProductCategory:
        return self.productCategoryRepository.get(
            ProductCategory(id=id)
        )
    
    def page(
            self, 
            pageSize: int = 25,
            startIndex: int = 0,
    ) -> List[ProductCategory]:
        return self.productCategoryRepository.page( 
            pageSize, 
            startIndex
        )
