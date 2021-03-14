from main import app
from src.bootloader.database.configuration.database import get_db
from src.domain.repository.enderecoRepository import *
from src.domain.repository.pessoaFisicaRepository import *
from src.domain.schema.enderecoSchema import EnderecoSchema, EnderecoCreate
from fastapi import Depends
from typing import List


@app.get("/enderecos", response_model=List[EnderecoSchema])
def read_enderecos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    enderecos = get_enderecos(db=db, skip=skip, limit=limit)
    return enderecos


@app.post("/endereco", response_model=EnderecoSchema)
def create_enderecos(endereco: EnderecoCreate, db: Session = Depends(get_db)) -> object:
    return create_endereco(db=db, endereco=endereco)

#ToDo:
#Criar edição e exclusã ode eventos do cache
#:ToDo