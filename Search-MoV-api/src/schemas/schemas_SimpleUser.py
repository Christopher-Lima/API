from datetime import date
from pydantic import BaseModel
from typing import Optional

### Esquema de usuário simples para listagem
class SimpleUser(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    age: date
    gender: str
    phone: Optional[str]

    class Config:
        orm_mode = True    