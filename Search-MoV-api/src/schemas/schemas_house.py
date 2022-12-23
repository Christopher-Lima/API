from pydantic import BaseModel
from typing import Optional
from src.schemas.schemas_SimpleUser import SimpleUser

###  Esquema de cadastro de imóvel
class House(BaseModel):
    id: Optional[int] = None
    uuid: Optional[str] = None
    type: str
    size: str   
    bedroom: Optional[int] = 0
    restroom: Optional[int] = 0
    furniture: bool = False
    cep: str
    state: str
    city: str
    district: str
    number: str
    reference: str    
    owner_id: int
    
    class Config:
        orm_mode = True


###  Esquema de imóvel para listagem
class SimpleHouse(BaseModel):
    type: str
    size: str   
    bedroom: Optional[int] = 0
    restroom: Optional[int] = 0
    furniture: bool = False
    state: str
    city: str
    
    class Config:
        orm_mode = True


###  Esquema de imóvel detalhado
class DetailHouse(BaseModel):
    type: str
    size: str   
    bedroom: Optional[int] = 0
    restroom: Optional[int] = 0
    furniture: bool = False
    cep: str
    state: str
    city: str
    district: str
    number: str
    reference: str
    owner: SimpleUser
    
    class Config:
        orm_mode = True
        
###  Esquema de imóvel para edição
class UpdateHouse(BaseModel):
    type: str
    size: str   
    bedroom: Optional[int] = 0
    restroom: Optional[int] = 0
    furniture: bool = False
    cep: str
    state: str
    city: str
    district: str
    number: str
    reference: str
    
    class Config:
        orm_mode = True