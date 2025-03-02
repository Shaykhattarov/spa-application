from typing import List
from fastapi import Depends
from sqlmodel import Session, select

from app.models.products import Product
from app.core.database import get_session

from sqlalchemy.exc import SQLAlchemyError


class ProductRepository:

    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    
    def create(self, product: Product) -> Product | None:
        self.session.add(product)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ... # logging
            return None
        self.session.refresh(product)
        return product

    def get(self, product: Product) -> Product:
        return self.session.get(Product, product.id)
    
    def page(self, skip: int, limit: int) -> List[Product]:
        statement = select(Product).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    