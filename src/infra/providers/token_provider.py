from datetime import datetime, timedelta
from jose import jwt

#Configurações
SECRET_KEY = '407cf29b336db365a45295b095976169'
ALGORITHM = 'HS256'
EXPIRES = 3000

def create_access_token(data: dict):
    data = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRES)
    data.update({'exp': expire})
    
    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

def check_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')