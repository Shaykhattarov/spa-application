from app.models.categories import ProductCategory
from app.core.database import get_session
from sqlmodel import Session, select
from sqlalchemy.orm import lazyload
from fastapi import Depends, Query
from typing import List


class ProductCategoryRepository:

    session: Session

    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def create(self, product_category: ProductCategory):

        self.session.add(product_category)
        self.session.commit()
        self.session.refresh(product_category)

        return product_category

    def get(self, product_category: ProductCategory) -> ProductCategory:
        return self.session.get(ProductCategory, product_category.id)
    
    def page(self, pageSize: int, startIndex: int) -> List[ProductCategory]:
        # offset_min = pageSize * startIndex
        # offset_max = (startIndex + 1) * pageSize
        statement = select(ProductCategory).offset(startIndex).limit(pageSize)
        return self.session.exec(statement).all()


