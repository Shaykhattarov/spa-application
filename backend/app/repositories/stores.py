from typing import List, Optional
from fastapi import Depends
from sqlmodel import Session, select

from app.models.stores import Store
from app.core.database import get_session

from sqlalchemy.exc import SQLAlchemyError


class StoreRepository:
    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, store: Store) -> Store | None:
        self.session.add(store)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ...  # logging
            return None
        self.session.refresh(store)
        return store

    def get(self, store: Store) -> Store:
        return self.session.get(Store, store.id)

    def page(self, skip: int, limit: int) -> List[Store]:
        statement = select(Store).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def put(self, store: Store) -> Optional[Store]:
        statement = select(Store).where(Store.id == store.id)
        old_store: Optional[Store] = self.session.exec(statement).one()

        if old_store is None:
            return None

        old_store.name = store.name
        old_store.address_id = store.address_id
        old_store.schedule_id = store.schedule_id
        old_store.scheme = store.scheme

        self.session.add(old_store)
        try:
            self.session.commit()
        except SQLAlchemyError:
            ...
            return None

        self.session.refresh(old_store)
        return old_store

    def delete(self, id: int) -> None:
        statement = select(Store).where(Store.id == id)
        store: Optional[Store] = self.session.exec(statement).one()
        self.session.delete(store)
        self.session.commit()
        return None
