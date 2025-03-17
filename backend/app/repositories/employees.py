from typing import List, Optional
from fastapi import Depends
from sqlmodel import Session, select

from app.models.employees import Employee
from app.core.database import get_session

from sqlalchemy.exc import SQLAlchemyError


class EmployeeRepository:
    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, model: Employee) -> Optional[Employee]:
        self.session.add(model)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ...  # logging
            return None
        self.session.refresh(model)
        return model

    def get(self, model: Employee):
        return self.session.get(Employee, model.id)

    def page(self, skip: int, limit: int):
        statement = select(Employee).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def put(self, model: Employee) -> Optional[Employee]:
        statement = select(Employee).where(Employee.id == model.id)
        old_model: Optional[Employee] = self.session.exec(statement).one()

        if old_model is None:
            return None

        old_model.name = model.name
        old_model.surname = model.surname
        old_model.patronymic = model.patronymic
        old_model.old = model.old
        old_model.phone = model.phone
        old_model.email = model.email
        old_model.store_id = model.store_id
        old_model.position_id = model.position_id

        self.session.add(old_model)
        try:
            self.session.commit()
        except SQLAlchemyError:
            return None

        self.session.refresh(old_model)
        return old_model

    def delete(self, id: int) -> None:
        statement = select(Employee).where(Employee.id == id)
        response: Optional[Employee] = self.session.exec(statement).one()
        self.session.delete(response)
        self.session.commit()
        return None
