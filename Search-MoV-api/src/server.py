from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import routers_user, routers_house, routers_announcement, routers_evaluation
from src.infra.sqlalchemy.config.database import create_db

create_db()

app = FastAPI()

## Origens aceitas para acessar a API
origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8080",
]

### Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### Rotas
app.include_router(routers_user.router, prefix="/auth")
app.include_router(routers_house.router)
app.include_router(routers_announcement.router)
app.include_router(routers_evaluation.router)