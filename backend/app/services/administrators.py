from datetime import timedelta, datetime, timezone
from fastapi import Depends, status
from typing import Annotated, Optional, List
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import Response, JSONResponse

from app.core.security import get_password_hash, verify_password, create_access_token

from app.schemas.jwtokens import JWToken
from app.models.administrators import Administrator
from app.repositories.administrators import AdministratorRepository
from app.schemas.administrators import AdministratorScheme, AdministratorUpdateScheme



class AdministratorService:

    repository: AdministratorRepository

    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    def __init__(self, repo: Annotated[AdministratorRepository, Depends()]):
        self.repository = repo

    def authenticate(self, form_data: OAuth2PasswordRequestForm):
        response = self.repository.getByLogin(login=form_data.username)
        if not response: 
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                headers={
                    "WWW-Authenticate": "Bearer"
                },
                detail="Incorrect username or password"
            )
        if not verify_password(form_data.password, response.password):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                headers={
                    "WWW-Authenticate": "Bearer"
                },
                detail="Incorrect username or password"
            )
        access_token_expires = timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            subject=response.login, 
            expires_delta=access_token_expires
        )
        return JWToken(
            access_token=access_token, 
            token_type='bearer'
        )
        

    def create(self, scheme: AdministratorScheme) -> Response:
        hashed_password: str = get_password_hash(scheme.password)
        response: Optional[Administrator] = self.repository.create(
            Administrator(
                name=scheme.name,
                surname=scheme.surname,
                login=scheme.login,
                password=hashed_password,
            )
        )

        if response is None:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={"location": f"/{Administrator.__tablename__}/{response.id}"},
        )

    def get(self, id: int) -> Response | JSONResponse:
        response = self.repository.get(Administrator(id=id))
        if response is None:
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        else:
            return JSONResponse(
                status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
            )

    def page(self, skip: int, limit: int) -> JSONResponse:
        response: List[Administrator] = self.repository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response,
        }
        return JSONResponse(content=jsonable_encoder(content))

    def put(self, scheme: AdministratorUpdateScheme) -> Response:
        hashed_password = get_password_hash(scheme.password)
        response: Optional[Administrator] = self.repository.put(
            Administrator(
                id=scheme.id,
                name=scheme.name,
                surname=scheme.surname,
                login=scheme.login,
                password=hashed_password,
            )
        )

        if response is None:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    def delete(self, id: int):
        self.repository.delete(id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
