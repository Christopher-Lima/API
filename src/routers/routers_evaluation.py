from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

##############################

from src.schemas.schemas_evaluation import *
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.repository_evaluation import RepositoryEvaluation

##############################

router = APIRouter()

## Rota para criar avaliação
@router.post('/evaluations', status_code=status.HTTP_201_CREATED, response_model=Evaluation)
def create_evaluation(evaluation: Evaluation, db: Session = Depends(get_db)):
    evaluation_created = RepositoryEvaluation(db).create(evaluation)
    return evaluation_created

## Rota para listar avaliações
@router.get('/evaluations', response_model=List[Evaluation])
def list_evaluation(db: Session = Depends(get_db)):
    evaluation = RepositoryEvaluation(db).list()
    return evaluation

## Rota para selecionar avaliação
@router.get('/evaluations/{evaluation_id}', response_model=Evaluation)
def get_evaluation(evaluation_id: int, db: Session = Depends(get_db)):
    selected_evaluation = RepositoryEvaluation(db).get(evaluation_id)
    if not selected_evaluation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Avaliação de id {evaluation_id} não encontrado ou não cadastrado.')
    return selected_evaluation

## Rota para editar avaliação
@router.put('/evaluations/{id}', response_model=Evaluation)
def update_evaluation(id: int, evaluation: Evaluation, db: Session = Depends(get_db)):
    selected_evaluation = RepositoryEvaluation(db).get(id)
    if not selected_evaluation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Avaliação de id {id} não foi encontrado ou não está cadastrado.')
    RepositoryEvaluation(db).edit(id, evaluation)
    evaluation.id = id
    return evaluation

## Rota para deletar avaliação
@router.delete('/evaluations/{evaluation_id}', status_code=status.HTTP_200_OK)
def remove_evaluation(evaluation_id: int, db: Session = Depends(get_db)):
    selected_evaluation = RepositoryEvaluation(db).get(evaluation_id)
    if not selected_evaluation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Avaliação de id {evaluation_id} não foi encontrado ou não está cadastrado.')    
    RepositoryEvaluation(db).remove(evaluation_id)
    return {"MSG": f"Avaliação de id {evaluation_id} removido com sucesso"}