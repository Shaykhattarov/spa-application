import jwt

from typing import Annotated

from sqlmodel import Session, select

from pydantic import ValidationError

from jwt.exceptions import InvalidTokenError

from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import Response

from app.core.database import engine
from app.core.config import settings

from app.models.administrators import Administrator
from app.schemas.jwtokens import JWTokenPayload




def get_session():
    with Session(engine) as session:
        yield session

reusable_oauth2= OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/administrators/login/access-token"
)

SessionDep = Annotated[Session, Depends(get_session)]
TokenDep = Annotated[str, Depends(reusable_oauth2)]

def get_current_administrator(session: SessionDep, token: TokenDep) -> Administrator:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = JWTokenPayload(**payload)
    except (InvalidTokenError, ValidationError):
        raise Response(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    administrator = session.exec(select(Administrator).where(Administrator.login == token_data.sub)).first()
    if not Administrator:
        raise Response(status_code=status.HTTP_404_NOT_FOUND, detail="Administrator not found")
    return administrator

CurrentAdministrator = Annotated[Administrator, Depends(get_current_administrator)]

# product_category_repository = ProductCategoryRepository()
# product_category_service = ProductCategoryService(product_category_repository)

# product_unit_repository = ProductUnitRepository()
# product_unit_service = ProductUnitService(product_unit_repository)
