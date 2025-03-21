from typing import Optional
from fastapi import Depends
from sqlmodel import Session, select

from app.models.supply_surcharges import SupplySurcharge
from app.core.database import get_session

from sqlalchemy.exc import SQLAlchemyError


class SupplySurchargeRepository:
    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, model: SupplySurcharge) -> Optional[SupplySurcharge]:
        self.session.add(model)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ...  # logging
            return None
        self.session.refresh(model)
        return model

    def get(self, model: SupplySurcharge):
        return self.session.get(SupplySurcharge, model.id)

    def page(self, skip: int, limit: int):
        statement = select(SupplySurcharge).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def put(self, model: SupplySurcharge) -> Optional[SupplySurcharge]:
        statement = select(SupplySurcharge).where(SupplySurcharge.id == model.id)
        old_model: Optional[SupplySurcharge] = self.session.exec(statement).one()

        if old_model is None:
            return None

        old_model.name = model.name
        old_model.supply_id = model.supply_id
        old_model.amount = model.amount

        self.session.add(old_model)
        try:
            self.session.commit()
        except SQLAlchemyError:
            return None

        self.session.refresh(old_model)
        return old_model

    def delete(self, id: int) -> None:
        statement = select(SupplySurcharge).where(SupplySurcharge.id == id)
        supplyItem: Optional[SupplySurcharge] = self.session.exec(statement).one()
        self.session.delete(supplyItem)
        self.session.commit()
        return None
