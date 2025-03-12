from typing import Optional
from fastapi import Depends
from sqlmodel import Session, select

from app.models.employee_positions import EmployeePosition
from app.core.database import get_session

from sqlalchemy.exc import SQLAlchemyError



class EmployeePositionRepository:

    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session


    def create(self, model: EmployeePosition) -> Optional[EmployeePosition]:
        self.session.add(model)
        try:
            self.session.commit()
        except SQLAlchemyError: 
            ... # logging
            return None
        self.session.refresh(model)
        return model
    
    def get(self, model: EmployeePosition): 
        return self.session.get(EmployeePosition, model.id)
    
    def page(self, skip: int, limit: int):
        statement = select(EmployeePosition).offset(skip).limit(limit)
        return self.session.exec(statement).all()
    
    def put(self, model: EmployeePosition) -> Optional[EmployeePosition]:
        statement = select(EmployeePosition).where(EmployeePosition.id == model.id)
        old_model: Optional[EmployeePosition] = self.session.exec(statement).one()

        if old_model is None:
            return None
        
        old_model.name = model.name

        self.session.add(old_model)
        try:
            self.session.commit()
        except SQLAlchemyError:
            return None
        
        self.session.refresh(old_model)
        return old_model


    def delete(self, id: int) -> None:
        statement = select(EmployeePosition).where(EmployeePosition.id == id)
        response: Optional[EmployeePosition] = self.session.exec(statement).one()
        self.session.delete(response)
        self.session.commit()
        return None