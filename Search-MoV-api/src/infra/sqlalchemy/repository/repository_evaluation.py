from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schemas.schemas_evaluation import *
from src.infra.sqlalchemy.models import models

class RepositoryEvaluation():
    
    def __init__(self, db: Session):
        self.db = db
    
    ## Criar uma avaliação no banco de dados
    def create(self, evaluation: Evaluation):
        create_evaluation = models.Evaluation(
            comment=evaluation.comment,
            rating=evaluation.rating
        )
        self.db.add(create_evaluation)
        self.db.commit()
        self.db.refresh(create_evaluation)
        return create_evaluation
    
    ## Listar avaliações escritas
    def list(self):
        list_evaluation = select(models.Evaluation)
        evaluation = self.db.execute(list_evaluation).scalars().all()
        return evaluation
    
    ## Selecionar uma avaliação escrita
    def get(self, evaluation_id: int):
        get_evaluation = select(models.Evaluation).where(models.Evaluation.id == evaluation_id)
        evaluation = self.db.execute(get_evaluation).scalars().first()
        return evaluation
    
    ## Editar uma avaliação escrita
    def edit(self, id: int, evaluation: Evaluation):
        update_evaluation = update(models.Evaluation).where(
            models.Evaluation.id==id).values(
                comment=evaluation.comment,
                rating=evaluation.rating
            )
        self.db.execute(update_evaluation)
        self.db.commit()
    
    ## Deleta uma avaliação escrita
    def remove(self, evaluation_id: int):
        delete_evaluation = delete(models.Evaluation).where(models.Evaluation.id==evaluation_id)
        self.db.execute(delete_evaluation)
        self.db.commit()