from sqlalchemy.orm import Session

from src.domain.entity.PessoaFisica import PessoaFisica
from src.domain.schema.pessoaFisicaSchema import PessoaFisicaCreate


def get_pessoas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PessoaFisica).offset(skip).limit(limit).all()


def get_pessoa_by_cpf(db: Session, cpf: str):
    return db.query(PessoaFisica).filter(PessoaFisica.cpf == cpf).first()


def create_pessoa(db: Session, pessoa: PessoaFisicaCreate):
    db_pessoa = PessoaFisica(**pessoa.dict())
    db.add(db_pessoa)
    db.commit()
    db.refresh(db_pessoa)
    return db_pessoa
