from typing import List, Optional
from fastapi import Depends
from sqlmodel import Session, select

from app.models.supplies import Supply
from app.core.database import get_session

from sqlalchemy.exc import SQLAlchemyError


class SupplyRepository:
    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, supply: Supply) -> Optional[Supply]:
        self.session.add(supply)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ...  # logging
            return None
        self.session.refresh(supply)
        return supply

    def get(self, product: Supply) -> Supply:
        return self.session.get(Supply, product.id)

    def page(self, skip: int, limit: int) -> List[Supply]:
        statement = select(Supply).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def put(self, supply: Supply) -> Optional[Supply]:
        statement = select(Supply).where(Supply.id == supply.id)
        old_supply: Optional[Supply] = self.session.exec(statement).one()

        if old_supply is None:
            return None

        old_supply.store_id = supply.store_id
        old_supply.supplier_id = supply.supplier_id
        old_supply.total_amount = supply.total_amount
        old_supply.date = supply.date

        self.session.add(old_supply)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ...
            return None

        self.session.refresh(old_supply)
        return old_supply

    def delete(self, id: int) -> None:
        statement = select(Supply).where(Supply.id == id)
        supply: Optional[Supply] = self.session.exec(statement).one()
        self.session.delete(supply)
        self.session.commit()
        return None
