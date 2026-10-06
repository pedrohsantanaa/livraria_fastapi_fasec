from fastapi import APIRouter, HTTPException, Depends
from app.schemas.livro import LivroResponse, LivroSchema
from app.database.connection import SessionLocal
from app.database.models import LivroModel
from app.schemas.livro import LivroCreate

from sqlalchemy.orm  import Session

from app.database.connection import get_db
from app.services import livro_service

router = APIRouter(
    prefix="/livros",
    tags=["livros"],
)

#listar-livros
@router.get("/")
async def listar_livros(
    db:Session = Depends(get_db)
):
  return livro_service.listar_livros(db)
 
#Adicionar Livros
@router.post("/" , response_model=LivroResponse)
async def adicionar_livro(
    livro: LivroCreate,
    db:Session = Depends(get_db)
    ):
    return livro_service.adicionar_livro(livro, db)
    
#atualizar-livro
@router.put("/{index}", response_model=LivroResponse)
async def atualizar_livro(
    index: int, 
    livro: LivroCreate,
    db:Session = Depends(get_db)
    ):

    livro_db = livro_service.atualizar_livro(index, livro, db)

    if not livro_db:
        raise HTTPException(status_code = 404, detail = "Livro não encontrado")

    return livro_db

#delete-livro
@router.delete("/{index}", response_model=LivroResponse)
async def deletar_livro(
    index: int,
    db:Session = Depends(get_db)
    ):

    removido = livro_service.remover_livro(index, db)

    db.close()

    if not removido:
         raise HTTPException(status_code = 404, detail = "Livro não encontrado")

    return {
        "message": "Livro removido com sucesso!!"
    }