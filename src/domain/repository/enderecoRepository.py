from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.domain.entity.endereco import Endereco
from src.domain.schema.enderecoSchema import EnderecoCreate


def get_enderecos(db: Session, skip: int = 0, limit: int = 100) -> object:
    return db.query(Endereco).offset(skip).limit(limit).all()


def create_endereco(db: Session, endereco: EnderecoCreate) -> Endereco:
    db_endereco = Endereco(**endereco.dict())
    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco


def endereco_exist(db: Session, endereco=EnderecoCreate):
    return db.query(Endereco).filter(
        and_(Endereco.cep.like(endereco.cep),
             Endereco.endereco.like(endereco.endereco),
             Endereco.numero.like(endereco.numero),
             Endereco.complemento.like(endereco.complemento),
             Endereco.bairro.like(endereco.bairro),
             Endereco.cidade.like(endereco.cidade),
             Endereco.estado.like(endereco.estado),
             )
    ).first()
