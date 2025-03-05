from typing import List, Optional
from fastapi import Depends
from sqlmodel import select, Session
from sqlalchemy.exc import SQLAlchemyError

from app.core.database import get_session
from app.models.suppliers import Supplier




class SupplierRepository:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, supplier: Supplier) -> Optional[Supplier]:
        self.session.add(supplier)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ...
            return None
        self.session.refresh(supplier)
        return supplier

    def get(self, supplier: Supplier) -> Optional[Supplier]: 
        return self.session.get(Supplier, supplier.id)

    def page(self, skip: int, limit: int) -> List[Supplier]:
        statement = select(Supplier).offset(skip).limit(limit)
        return self.session.exec(statement).all()
    
    def put(self, supplier: Supplier) -> Optional[Supplier]:
        statement = select(Supplier).where(Supplier.id == supplier.id)
        old_supplier: Optional[Supplier] = self.session.exec(statement).one()

        if old_supplier is None:  return None

        old_supplier.name = supplier.name
        old_supplier.category_id = supplier.category_id

        self.session.add(old_supplier)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ...
            return None
        
        self.session.refresh(old_supplier)
        return old_supplier