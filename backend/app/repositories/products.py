from app.models.products import Product
from app.core.database import get_session
from sqlmodel import Session
from fastapi import Depends


class ProductRepository:

    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    
    def create(self, product: Product) -> Product:
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product
    
    def get(self): ...
    
    def patch(self): ...

    def delete(self): ...

    