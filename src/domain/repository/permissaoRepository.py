from sqlalchemy import and_
from sqlalchemy.orm import Session
from src.domain.entity.permissao import Permissao
from src.domain.schema.permissaoSchema import PermissaoCreate


def get_permissoes(db: Session, skip: int = 0, limit: int = 100) -> object:
    return db.query(Permissao).offset(skip).limit(limit).all()


def create_permissao(db: Session, permissao: PermissaoCreate) -> object:
    db_permissao = Permissao(**permissao.dict())
    db.add(db_permissao)
    db.commit()
    db.refresh(db_permissao)
    return db_permissao

def permissao_exist(db: Session, permissao=PermissaoCreate):
    return db.query(Permissao).filter(
        and_(Permissao.nome.like(permissao.nome),
             Permissao.descricao.like(permissao.descricao)
             )
    ).first()
