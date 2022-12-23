from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from src.schemas.schemas_SimpleUser import SimpleUser
from src.schemas.schemas_house import SimpleHouse

###  Esquema de cadastro de usuário
class User(BaseModel):  
    id: Optional[int] = None
    uuid: Optional[str] = None
    first_name: str
    last_name: Optional[str] = None
    age: date
    gender: str
    cpf_cnpj: Optional[str] = None
    phone: Optional[str] = None
    email: str
    password: str

    class Config:
        orm_mode = True

### Esquema de usuário detalhado para seleção
class DetailUser(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: Optional[str] = None
    age: date
    gender: str
    cpf_cnpj: Optional[str] = None
    phone: Optional[str]
    email: str
    house: List[SimpleHouse] = []

    class Config:
        orm_mode = True


### Esquema de login de usuário
class UserLogin(BaseModel):
    email: str
    password: str

### Esquema de sucesso ao fazer login
class UserLogged(BaseModel):
    user: SimpleUser
    access_token: str
    