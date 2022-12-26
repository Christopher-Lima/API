from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

##############################

from src.schemas.schemas_user import *
from src.schemas.schemas_SimpleUser import SimpleUser
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.repository_user import RepositoryUser
from src.infra.providers import hash_provider, token_provider
from src.routers.auth_utils import get_user_logged

##############################

router = APIRouter()

## Rota para criação de usuario
@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=SimpleUser)
def create_user(user: User, db: Session = Depends(get_db)):
    # verificar se já existe
    email_located = RepositoryUser(db).get(user.email)
    
    if email_located:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Já existe uma conta com esse email em uso.')
    
    # criar novo usuário
    user.password = hash_provider.generate_hash(user.password)
    user_created = RepositoryUser(db).create(user)
    return user_created

## Rota para listar usuários cadastrados
@router.get('/users', response_model=List[SimpleUser])
def list_users(db: Session = Depends(get_db)):
    users = RepositoryUser(db).list()
    return users

## Rota para selecionar usuário cadastrado
@router.get('/users/{email_user}', response_model=DetailUser)
def get_user(email_user: str, db: Session = Depends(get_db)):
    user = RepositoryUser(db).get(email_user)
    return user

## Rota para editar usuário cadastrado
@router.put('/users/{id}', response_model=DetailUser)
def update_user(id: int, user: DetailUser,  db: Session = Depends(get_db)):
    RepositoryUser(db).edit(id, user)
    user.id = id
    return user

## Rota para deletar usuario cadastrado
@router.delete('/users/{user_id}')
def remove_user(user_id: int, db: Session = Depends(get_db)):
    RepositoryUser(db).remove(user_id)
    return {"MSG": "Usuário removido com sucesso"}

@router.post('/token', response_model=UserLogged)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    email = user_login.email
    password = user_login.password
    user = RepositoryUser(db).get(email)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email ou senha estão incorretos!')
    
    password_valid = hash_provider.check_hash(password, user.password)
    
    if not password_valid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email ou senha estão incorretos!')
    
    token = token_provider.create_access_token({'sub': user.email})
    return UserLogged(user=user, access_token=token)

@router.get('/me', response_model=SimpleUser)
def me(user: User = Depends(get_user_logged)):
    return user