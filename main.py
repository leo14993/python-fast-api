from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/enderecos/", response_model=List[schemas.Endereco])
def read_enderecos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    enderecos = crud.get_enderecos(db, skip=skip, limit=limit)
    return enderecos

@app.get("/pessoas/", response_model=List[schemas.PessoaFisica])
def read_pessoas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pessoas = crud.get_pessoas(db, skip=skip, limit=limit)
    return pessoas