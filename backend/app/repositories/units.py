from app.models.units import ProductUnit
from app.core.database import get_session
from sqlmodel import Session, select
from fastapi import Depends
from typing import List



class ProductUnitRepository:

    session: Session

    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def create(self, product_unit: ProductUnit):
        self.session.add(product_unit)
        self.session.commit()
        self.session.refresh(product_unit)

        return product_unit

    def get(self, product_unit: ProductUnit) -> ProductUnit:
        return self.session.get(ProductUnit, product_unit.id)
    
    def page(self, pageSize: int, startIndex: int) -> List[ProductUnit]:
        statement = select(ProductUnit).offset(startIndex).limit(pageSize)
        return self.session.exec(statement).all()