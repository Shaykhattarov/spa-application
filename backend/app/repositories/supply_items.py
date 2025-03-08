from typing import List, Optional
from fastapi import Depends
from sqlmodel import Session, select

from app.models.supply_items import SupplyItem
from app.core.database import get_session

from sqlalchemy.exc import SQLAlchemyError



class SupplyItemRepository:

    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, supplyItem: SupplyItem) -> SupplyItem | None:
        self.session.add(supplyItem)
        try:
            self.session.commit()
        except SQLAlchemyError: 
            ... # logging
            return None
        self.session.refresh(supplyItem)
        return supplyItem

    def get(self, supplyItem: SupplyItem): 
        return self.session.get(SupplyItem, supplyItem.id)
    
    def page(self, skip: int, limit: int):
        statement = select(SupplyItem).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def put(self, supplyItem: SupplyItem) -> Optional[SupplyItem]:
        statement = select(SupplyItem).where(SupplyItem.id == supplyItem.id)
        old_supply_item: Optional[SupplyItem] = self.session.exec(statement).one()

        if old_supply_item is None:
            return None
        
        old_supply_item.supply_id = supplyItem.supply_id
        old_supply_item.product_id = supplyItem.product_id
        old_supply_item.quantity = supplyItem.quantity
        old_supply_item.price = supplyItem.price

        self.session.add(old_supply_item)
        try:
            self.session.commit()
        except SQLAlchemyError:
            return None
        
        self.session.refresh(old_supply_item)
        return old_supply_item


    def delete(self, id: int) -> None:
        statement = select(SupplyItem).where(SupplyItem.id == id)
        supplyItem: Optional[SupplyItem] = self.session.exec(statement).one()
        self.session.delete(supplyItem)
        self.session.commit()
        return None