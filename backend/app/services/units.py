from fastapi import Depends
from typing import List

from app.repositories.units import ProductUnitRepository
from app.schemas.units import ProductUnitScheme
from app.models.units import ProductUnit

class ProductUnitService:

    productUnitRepository: ProductUnitRepository

    def __init__(self, productUnitRepository: ProductUnitRepository = Depends()) -> None:
        self.productUnitRepository = productUnitRepository

    def create(self, unit: ProductUnitScheme) -> ProductUnit:
        return self.productUnitRepository.create(
            ProductUnit(name=unit.name, abbreviation=unit.abbreviation)
        )
    
    def get(self, id: int) -> ProductUnit:
        return self.productUnitRepository.get(
            ProductUnit(id=id)
        )
    
    def page(
            self, 
            pageSize: int = 25,
            startIndex: int = 0,
    ) -> List[ProductUnit]:
        return self.productUnitRepository.page( 
            pageSize, 
            startIndex
        )