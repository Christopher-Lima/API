from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

##############################

from src.schemas.schemas_house import *
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.repository_house import RepositoryHouse

##############################

router = APIRouter()

## Rota para criação de imóvel
@router.post('/houses', status_code=status.HTTP_201_CREATED, response_model=House)
def create_house(house: House, db: Session = Depends(get_db)):
    house_created = RepositoryHouse(db).create(house)
    return house_created

## Rota para listagem de imóveis cadastrados
@router.get('/houses', response_model=List[SimpleHouse])
def list_house(db: Session = Depends(get_db)):
    houses = RepositoryHouse(db).list()
    return houses

## Rota para seleção de imóvel cadastrado
@router.get('/houses/{house_id}', response_model=DetailHouse)
def get_house(house_id: int, db: Session = Depends(get_db)):
    selected_house = RepositoryHouse(db).get(house_id)
    if not selected_house:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Imóvel de id {house_id} não encontrado ou não cadastrado.')
    return selected_house

## Rota para a edição de um imóvel cadastrado
@router.put('/houses/{id}', response_model=UpdateHouse)
def update_house(id: int, house: House, db: Session = Depends(get_db)):
    selected_house = RepositoryHouse(db).get(id)
    if not selected_house:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Imóvel de id {id} não foi encontrado ou não está cadastrado.')
    RepositoryHouse(db).edit(id, house)
    house.id = id
    return house

## Rota para remover imóvel cadastrado
@router.delete('/houses/{house_id}', status_code=status.HTTP_200_OK)
def remove_house(house_id: int, db: Session = Depends(get_db)):
    selected_house = RepositoryHouse(db).get(house_id)
    if not selected_house:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Imóvel de id {house_id} não foi encontrado ou não está cadastrado.')    
    RepositoryHouse(db).remove(house_id)
    return {"MSG": f"Imóvel de id {house_id} removido com sucesso"}