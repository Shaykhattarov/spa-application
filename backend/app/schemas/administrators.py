from pydantic import BaseModel



class AdministratorScheme(BaseModel):
    name: str
    surname: str
    login: str
    password: str



class AdministratorAuthScheme(BaseModel):
    login: str
    password: str


class AdministratorUpdateScheme(AdministratorScheme):
    id: int


