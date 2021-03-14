from sqlalchemy.orm import Session

from src.domain.entity.pessoaFisica import PessoaFisica, PessoaEndereco
from src.domain.schema.pessoaFisicaSchema import PessoaFisicaCreate


def get_pessoas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PessoaFisica).offset(skip).limit(limit).all()


def get_pessoa_by_cpf(db: Session, cpf: str):
    return db.query(PessoaFisica).filter(PessoaFisica.cpf == cpf).first()


def cpf_exists(db: Session, cpf: str):
    return db.query(PessoaFisica.cpf).filter(PessoaFisica.cpf == cpf).first()


def create_pessoa(db: Session, pessoa: PessoaFisicaCreate):

    db_pessoa = PessoaFisica(**pessoa.dict())
    db.add(db_pessoa)
    db.commit()
    db.refresh(db_pessoa)
    return db_pessoa


def edit_pessoa(db: Session, pessoa: PessoaFisicaCreate):
    db_pessoa = PessoaFisica(**pessoa.dict())
    db.query(PessoaFisica).filter(PessoaFisica.cpf == pessoa.cpf).update(pessoa.dict())
    db.commit()
    return db_pessoa


def delete_pessoa(db: Session, pessoa: PessoaFisicaCreate):
    db_pessoa = PessoaFisica(**pessoa.dict())
    db.query(PessoaFisica).filter(PessoaFisica.cpf == pessoa.cpf).delete(synchronize_session=False)
    db.commit()
    return "deletado"


def add_endereco_pessoa(db: Session, pessoa_id: int, endereco_id: int):

    db_pessoa_endereco = PessoaEndereco(pessoa_id=pessoa_id, endereco_id=endereco_id)
    db.add(db_pessoa_endereco)
    db.commit()
    db.refresh(db_pessoa_endereco)

    return "Endereço associado a pessoa física com sucesso!"
