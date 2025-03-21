from typing import Optional
from fastapi import Depends
from sqlmodel import Session, select

from app.models.administrators import Administrator
from app.core.database import get_session

from sqlalchemy.exc import SQLAlchemyError



class AdministratorRepository:
    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, model: Administrator) -> Optional[Administrator]:
        self.session.add(model)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ...  # logging
            return None
        self.session.refresh(model)
        return model

    def get(self, model: Administrator):
        return self.session.get(Administrator, model.id)
    
    def getByLogin(self, login: str) -> Optional[Administrator]:
        statement = select(Administrator).where(Administrator.login == login)
        response = self.session.exec(statement).first()
        return response

    def page(self, skip: int, limit: int):
        statement = select(Administrator).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def put(self, model: Administrator) -> Optional[Administrator]:
        statement = select(Administrator).where(Administrator.id == model.id)
        old_model: Optional[Administrator] = self.session.exec(statement).one()

        if old_model is None:
            return None

        old_model.name = model.name
        old_model.surname = model.surname
        old_model.login = model.login
        old_model.password = model.password

        self.session.add(old_model)
        try:
            self.session.commit()
        except SQLAlchemyError:
            return None

        self.session.refresh(old_model)
        return old_model

    def delete(self, id: int) -> None:
        statement = select(Administrator).where(Administrator.id == id)
        supplyItem: Optional[Administrator] = self.session.exec(statement).one()
        self.session.delete(supplyItem)
        self.session.commit()
        return None
