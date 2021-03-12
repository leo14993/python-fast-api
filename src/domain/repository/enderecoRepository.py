from sqlalchemy.orm import Session

from src.domain.entity.Endereco import Endereco
from src.domain.schema.enderecoSchema import EnderecoCreate


def get_enderecos(db: Session, skip: int = 0, limit: int = 100) -> object:
    return db.query(Endereco).offset(skip).limit(limit).all()


def create_endereco(db: Session, endereco: EnderecoCreate) -> object:
    db_endereco = Endereco(**endereco.dict())
    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco
