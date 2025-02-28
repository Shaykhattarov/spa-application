from app.models.categories import ProductCategory
from app.core.database import get_session
from sqlmodel import Session, select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import Depends, Query
from typing import List


class ProductCategoryRepository:

    session: Session

    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def create(self, product_category: ProductCategory) -> ProductCategory | None:
        self.session.add(product_category)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ... # logging
            return None
        self.session.refresh(product_category)
        return product_category

    def get(self, product_category: ProductCategory) -> ProductCategory:
        return self.session.get(ProductCategory, product_category.id)
    
    def page(self, skip: int, limit: int) -> List[ProductCategory]:
        statement = select(ProductCategory).offset(skip).limit(limit)
        return self.session.exec(statement).all()


