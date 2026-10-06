from fastapi import FastAPI, HTTPException
from app.schemas.livro import LivroSchema
from app.routers import livros

from app.database.connection import engine
from app.database.models import Base

from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(livros.router)

#rota-inicial
@app.get("/")
async def home():
    return {"message": "Bem-vindo à API de Livros!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)