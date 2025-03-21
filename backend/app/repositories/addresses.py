from typing import Optional
from fastapi import Depends
from sqlmodel import Session, select

from app.models.addresses import Addresses
from app.core.database import get_session

from sqlalchemy.exc import SQLAlchemyError


class AddressesRepository:
    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, model: Addresses) -> Optional[Addresses]:
        self.session.add(model)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ...  # logging
            return None
        self.session.refresh(model)
        return model

    def get(self, model: Addresses):
        return self.session.get(Addresses, model.id)

    def page(self, skip: int, limit: int):
        statement = select(Addresses).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def put(self, model: Addresses) -> Optional[Addresses]:
        statement = select(Addresses).where(Addresses.id == model.id)
        old_model: Optional[Addresses] = self.session.exec(statement).one()

        if old_model is None:
            return None

        old_model.city = model.city
        old_model.street = model.street
        old_model.house = model.house
        old_model.apt = model.apt

        self.session.add(old_model)
        try:
            self.session.commit()
        except SQLAlchemyError:
            return None

        self.session.refresh(old_model)
        return old_model

    def delete(self, id: int) -> None:
        statement = select(Addresses).where(Addresses.id == id)
        supplyItem: Optional[Addresses] = self.session.exec(statement).one()
        self.session.delete(supplyItem)
        self.session.commit()
        return None
