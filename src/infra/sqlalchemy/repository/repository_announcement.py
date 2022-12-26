from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schemas.schemas_announcement import *
from src.infra.sqlalchemy.models import models

class RepositoryAnnouncement():
    
    def __init__(self, db: Session):
        self.db = db
    
    ## Criar um anúncio no banco de dados
    def create(self, announcement: Announcement):
        create_announcement = models.Announcement(
            name=announcement.name,
            type=announcement.type,
            rent_period=announcement.rent_period,
            available=announcement.available
        )
        self.db.add(create_announcement)
        self.db.commit()
        self.db.refresh(create_announcement)
        return create_announcement
    
    ## Listar anúncios cadastrados
    def list(self):
        list_announcement = select(models.Announcement)
        announcement = self.db.execute(list_announcement).scalars().all()
        return announcement
    
    ## Selecionar um anúncio cadastrado
    def get(self, announcement_id: int):
        get_announcement = select(models.Announcement).where(models.Announcement.id == announcement_id)
        announcement = self.db.execute(get_announcement).scalars().first()
        return announcement
    
    ## Editar um anúncio cadastrado
    def edit(self, id: int, announcement: Announcement):
        update_announcement = update(models.Announcement).where(
            models.Announcement.id==id).values(
                name=announcement.name,
                type=announcement.type,
                rent_period=announcement.rent_period,
                available=announcement.available
            )
        self.db.execute(update_announcement)
        self.db.commit()
    
    ## Deleta um anúncio cadastrado
    def remove(self, announcement_id: int):
        delete_announcement = delete(models.Announcement).where(models.Announcement.id==announcement_id)
        self.db.execute(delete_announcement)
        self.db.commit()