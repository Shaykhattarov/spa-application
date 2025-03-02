from sqlmodel import create_engine, SQLModel, Session
from app.core.config import settings



engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def get_session():
    with Session(engine) as session:
        yield session

