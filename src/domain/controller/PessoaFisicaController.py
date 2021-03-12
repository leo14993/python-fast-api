from main import app
from src.bootloader.database.configuration.database import get_db
from src.domain.repository.pessoaFisicaRepository import *
from src.domain.schema.pessoaFisicaSchema import PessoaFisicaCreate, PessoaFisica
from fastapi import Depends
from typing import List


@app.get("/pessoas", response_model=List[PessoaFisica])
def read_pessoas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pessoas = get_pessoas(db=db, skip=skip, limit=limit)
    return pessoas


@app.post("/pessoas", response_model=PessoaFisica)
def create_pessoas(pessoa: PessoaFisicaCreate, db: Session = Depends(get_db)):
    # db_pessoa = crud.get_pessoa_by_cpf(db, cpf=pessoa.cpf)
    # if db_pessoa:
    #     raise HTTPException(status_code=400, detail="CPF already registered")
    return create_pessoa(db=db, pessoa=pessoa)
