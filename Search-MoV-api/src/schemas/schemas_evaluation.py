from pydantic import BaseModel
from typing import Optional

### Esquema de criação de avaliações
class Evaluation(BaseModel):
    id: Optional[int] = None
    uuid: Optional[str] = None
    comment: str
    rating: float
    owner_id: int
    announcement_id: int
    
    class Config:
        orm_mode = True