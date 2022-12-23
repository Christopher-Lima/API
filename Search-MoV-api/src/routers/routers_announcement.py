from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

##############################

from src.schemas.schemas_announcement import *
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.repository_announcement import RepositoryAnnouncement

##############################

router = APIRouter()

## Rota para criar anúncio
@router.post('/announcements', status_code=status.HTTP_201_CREATED, response_model=Announcement)
def create_announcement(announcement: Announcement, db: Session = Depends(get_db)):
    announcement_created = RepositoryAnnouncement(db).create(announcement)
    return announcement_created

## Rota para listar anúncio
@router.get('/announcements', response_model=List[Announcement])
def list_announcement(db: Session = Depends(get_db)):
    announcement = RepositoryAnnouncement(db).list()
    return announcement

## Rota para selecionar anúncio
@router.get('/announcements/{announcement_id}', response_model=Announcement)
def get_announcement(announcement_id: int, db: Session = Depends(get_db)):
    selected_announcement = RepositoryAnnouncement(db).get(announcement_id)
    if not selected_announcement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Anúncio de id {announcement_id} não encontrado ou não cadastrado.')
    return selected_announcement

## Rota para editar anúncio
@router.put('/announcements/{id}', response_model=Announcement)
def update_announcement(id: int, announcement: Announcement, db: Session = Depends(get_db)):
    selected_announcement = RepositoryAnnouncement(db).get(id)
    if not selected_announcement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Anúncio de id {id} não foi encontrado ou não está cadastrado.')
    RepositoryAnnouncement(db).edit(id, announcement)
    announcement.id = id
    return announcement

## Rota para deletar anúncio
@router.delete('/announcements/{announcement_id}', status_code=status.HTTP_200_OK)
def remove_announcement(announcement_id: int, db: Session = Depends(get_db)):
    selected_announcement = RepositoryAnnouncement(db).get(announcement_id)
    if not selected_announcement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Anúncio de id {announcement_id} não foi encontrado ou não está cadastrado.')    
    RepositoryAnnouncement(db).remove(announcement_id)
    return {"MSG": f"Anúncio de id {announcement_id} removido com sucesso"}