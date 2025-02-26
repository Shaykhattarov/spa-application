from app.schemas.products import ProductScheme, ProductCategoryScheme
from app.core.database import get_session
from sqlmodel import Session


class ProductRepository:
    @classmethod
    def add_one(cls, product: ProductScheme):
        session: Session = get_session()

        session.add()
        session.commit()



        
    