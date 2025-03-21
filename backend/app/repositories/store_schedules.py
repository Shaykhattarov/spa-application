from typing import Optional
from fastapi import Depends
from sqlmodel import Session, select

from app.models.store_schedules import StoreSchedule
from app.core.database import get_session

from sqlalchemy.exc import SQLAlchemyError


class StoreScheduleRepository:
    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, model: StoreSchedule) -> Optional[StoreSchedule]:
        self.session.add(model)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ...  # logging
            return None
        self.session.refresh(model)
        return model

    def get(self, model: StoreSchedule):
        return self.session.get(StoreSchedule, model.id)

    def page(self, skip: int, limit: int):
        statement = select(StoreSchedule).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def put(self, model: StoreSchedule) -> Optional[StoreSchedule]:
        statement = select(StoreSchedule).where(StoreSchedule.id == model.id)
        old_model: Optional[StoreSchedule] = self.session.exec(statement).one()

        if old_model is None:
            return None

        old_model.day_of_week = model.day_of_week
        old_model.open_time = model.open_time
        old_model.close_time = model.close_time

        self.session.add(old_model)
        try:
            self.session.commit()
        except SQLAlchemyError:
            return None

        self.session.refresh(old_model)
        return old_model

    def delete(self, id: int) -> None:
        statement = select(StoreSchedule).where(StoreSchedule.id == id)
        supplyItem: Optional[StoreSchedule] = self.session.exec(statement).one()
        self.session.delete(supplyItem)
        self.session.commit()
        return None
