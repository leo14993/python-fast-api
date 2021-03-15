from main import app
from src.bootloader.database.configuration.database import get_db
from src.domain.repository.pessoaFisicaRepository import *
from src.domain.schema.pessoaFisicaSchema import PessoaFisicaCreate, PessoaFisicaSchema, PessoaFisicaCPF, \
    PessoaFisicaBase, PessoaFisicaEndereco
from fastapi import Depends
from typing import List

from src.domain.service.pessoaService import PessoaService


@app.get("/pessoas", response_model=List[PessoaFisicaSchema])
def list_todas_pessoas(db: Session = Depends(get_db)):
    pessoa_service = PessoaService(db)
    pessoas = pessoa_service.get_all()
    return pessoas


@app.post("/get_pessoa", response_model=PessoaFisicaSchema)
def list_pessoa(cpf: PessoaFisicaCPF, db: Session = Depends(get_db)):
    pessoa_service = PessoaService(db)
    pessoa = pessoa_service.get(cpf)
    return pessoa


@app.post("/pessoa", response_model=PessoaFisicaSchema)
def create_pessoa(pessoa: PessoaFisicaCreate, db: Session = Depends(get_db)):
    pessoa_service = PessoaService(db)
    return pessoa_service.create(pessoa=pessoa)

@app.put("/pessoa", response_model=PessoaFisicaSchema)
def update_pessoa(pessoa: PessoaFisicaBase, db: Session = Depends(get_db)):
    pessoa_service = PessoaService(db)
    return pessoa_service.update(pessoa=pessoa)

@app.delete("/pessoa")
def delete_pessoa(pessoa: PessoaFisicaCPF, db: Session = Depends(get_db)):
    pessoa_service = PessoaService(db)
    return pessoa_service.delete(pessoa=pessoa)

@app.post("/pessoa/endereco", response_model=dict)
def create_endereco_pessoa(pessoa: PessoaFisicaEndereco, db: Session = Depends(get_db)):
    pessoa_service = PessoaService(db)
    return pessoa_service.create_endereco_pessoa(pessoa=pessoa)
