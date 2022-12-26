from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette import status
from jose import JWTError

from src.infra.sqlalchemy.repository.repository_user import RepositoryUser
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def get_user_logged(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')
    
    try:
        email = token_provider.check_access_token(token)
    except JWTError:
        raise exception

    if not email:
        raise exception

    user = RepositoryUser(db).get(email)

    if not user:
        raise exception

    return user
