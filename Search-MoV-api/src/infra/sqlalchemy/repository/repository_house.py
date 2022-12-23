from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schemas.schemas_house import *
from src.infra.sqlalchemy.models import models

class RepositoryHouse():
    
    def __init__(self, db: Session):
        self.db = db

    ## Criar um imóvel no banco de dados
    def create(self, house: House):
        create_house = models.House (
            type=house.type,
            size=house.size,
            bedroom=house.bedroom,
            restroom=house.restroom,
            furniture=house.furniture,
            cep=house.cep,
            state=house.state,
            city=house.city,
            district=house.district,
            number=house.number,
            reference=house.reference,
            owner_id=house.owner_id)
        self.db.add(create_house)
        self.db.commit()
        self.db.refresh(create_house)
        return create_house
    
    ## Listar imóveis cadastrados
    def list(self):
        list_house = select(models.House)        
        houses = self.db.execute(list_house).scalars().all()
        return houses
    
    ## Selecionar um imóvel cadastrado
    def get(self, house_id: int):
        get_house = select(models.House).where(models.House.id == house_id)
        house = self.db.execute(get_house).scalars().first()
        return house
    
    ## Editar um imóvel cadastrado
    def edit(self, id: int, house: House):
        update_house = update(models.House).where(
            models.House.id==id).values(
                type=house.type,
                size=house.size,
                bedroom=house.bedroom,
                restroom=house.restroom,
                furniture=house.furniture,
                cep=house.cep,
                state=house.state,
                city=house.city,
                district=house.district,
                number=house.number,
                reference=house.reference
                )
        self.db.execute(update_house)
        self.db.commit()
    
    ## Remove um imóvel cadastrado
    def remove(self, house: int):
        delete_house = delete(models.House).where(models.House.id==house)
        self.db.execute(delete_house)
        self.db.commit()