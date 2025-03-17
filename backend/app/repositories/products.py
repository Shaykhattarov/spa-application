from typing import List, Optional
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
            ...  # logging
            return None
        self.session.refresh(product)
        return product

    def get(self, product: Product) -> Product:
        return self.session.get(Product, product.id)

    def page(self, skip: int, limit: int) -> List[Product]:
        statement = select(Product).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def put(self, product: Product) -> Optional[Product]:
        statement = select(Product).where(Product.id == product.id)
        old_product: Optional[Product] = self.session.exec(statement).one()

        if old_product is None:
            return None

        old_product.name = product.name
        old_product.category_id = product.category_id
        old_product.unit_id = product.unit_id
        old_product.value = product.value
        old_product.retail_price = product.retail_price

        self.session.add(old_product)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ...
            return None

        self.session.refresh(old_product)
        return old_product

    def delete(self, id: int) -> None:
        statement = select(Product).where(Product.id == id)
        product: Optional[Product] = self.session.exec(statement).one()
        self.session.delete(product)
        self.session.commit()
        return None
