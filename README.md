# Search-MoV-api
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
## Como rodar o projeto em sua maquina

**Requisitos:**
Python 3.11.0

**Passos:**
1º - Crie um ambiente virtual python. Vá no terminal e digite:
```
    python -m venv virtual
```
2º - Entre no ambiente virtual com o comando:
```
    virtual\Scripts\activate.ps1

or

    virtual\Scripts\activate.bat

or

    virtual\Scripts\activate
```
3º - Agora faça a instalação do FastAPI, Uvicorn, SQL Alchemy e Alembic:
```
    pip install fastapi sqlalchemy "uvicorn[standard]" alembic passlib[bcrypt] python-jose[cryptography]
```
4º - Com o ambiente virtual ativado, navegue até a página do proejto e digite:
```
    uvicorn src.server:app --reload --reload-dir=src
```
5º - Abra o navegador e acesse o localhost para confirmar que esta funcionando da forma devida:
```
    http://localhost:8000/docs
```



``` Usando o Alembic:
digite no terminal
    alembic revision --autogenerate -m "Nome da Revisão"
    alembic upgrade head
Assim as alterações serão feitas no banco de dados
```

***Observações:***
* Sempre que for abrir o projeto, repita os passos 2 e 4;
* Crie o ambiente virtual em uma pasta com um nivel anterior ao seu projeto, para ficar mais pratico ativa-lo.
* Para fechar o ambiente virtual, digite "deactivate" no terminal, e para fechar o uvicorn, aperte ctrl+c.