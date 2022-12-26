from pydantic import BaseModel
from typing import Optional

### Esquema de criação de anúncios
class Announcement(BaseModel):
    id: Optional[int] = None
    uuid: Optional[str] = None
    name: str    
    type: str
    rent_period: str
    available: bool = False
    owner_id: int
    house_id: int

    class Config:
        orm_mode = True