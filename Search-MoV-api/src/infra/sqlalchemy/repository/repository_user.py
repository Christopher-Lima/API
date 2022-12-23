from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schemas.schemas_user import *
from src.infra.sqlalchemy.models import models

class RepositoryUser():
    
    def __init__(self, db: Session):
        self.db = db
    
    ## Criar um usuário no banco de dados
    def create(self, user: User):
        create_user = models.User(
            first_name=user.first_name,
            last_name=user.last_name,
            age=user.age,
            gender=user.gender,
            cpf_cnpj=user.cpf_cnpj,
            phone=user.phone,            
            email=user.email,
            password=user.password   
        )
        self.db.add(create_user)
        self.db.commit()
        self.db.refresh(create_user)
        return create_user
    
    ## Listar usuários cadastrados
    def list(self):
        list_users = select(models.User)
        users = self.db.execute(list_users).scalars().all()
        return users
    
    ## Selecionar um usuário cadastrado
    def get(self, email_user: str):
        get_user = select(models.User).where(models.User.email == email_user)
        user = self.db.execute(get_user).scalars().first()
        return user
    
    ## Selecionar um usuário cadastrado
    def get_login(self, email: str):
        get_user = select(models.User).where(models.User.email == email)
        return self.db.execute(get_user).scalars().first()
    
    ## Editar um usuário cadastrado
    def edit(self, id: int, user: DetailUser):
        update_user = update(models.User).where(
            models.User.id==id).values(
                first_name=user.first_name,
                last_name=user.last_name,
                age=user.age,
                gender=user.gender,
                cpf_cnpj=user.cpf_cnpj,
                phone=user.phone
            )
        self.db.execute(update_user)
        self.db.commit()
    
    ## Deleta um usuário cadastrado
    def remove(self, user_id: int):
        delete_user = delete(models.User).where(models.User.id==user_id)
        self.db.execute(delete_user)
        self.db.commit()