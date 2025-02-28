from app.models.units import ProductUnit
from app.core.database import get_session
from sqlmodel import Session, select
from fastapi import Depends
from typing import List
from sqlalchemy.exc import SQLAlchemyError



class ProductUnitRepository:

    session: Session

    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def create(self, product_unit: ProductUnit) -> ProductUnit | None:
        self.session.add(product_unit)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ... # logging
            return None
        self.session.refresh(product_unit)
        return product_unit

    def get(self, product_unit: ProductUnit) -> ProductUnit:
        return self.session.get(ProductUnit, product_unit.id)
    
    def page(self, skip: int, limit: int) -> List[ProductUnit]:
        statement = select(ProductUnit).offset(skip).limit(limit)
        return self.session.exec(statement).all()