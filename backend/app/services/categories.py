from fastapi import Depends
from typing import Optional, List

from app.models.categories import ProductCategory
from app.repositories.categories import ProductCategoryRepository
from app.schemas.categories import ProductCategoryScheme



class ProductCategoryService:

    productCategoryRepository: ProductCategoryRepository

    def __init__(self, productCategoryRepository: ProductCategoryRepository = Depends()) -> None:
        self.productCategoryRepository = productCategoryRepository

    def create(self, category: ProductCategoryScheme) -> ProductCategory:
        return self.productCategoryRepository.create(ProductCategory(name=category.name))
    
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
