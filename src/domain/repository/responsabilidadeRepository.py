from sqlalchemy.orm import Session

from src.domain.entity.responsabilidade import Responsabilidade, ResponsabilidadePermissao
from src.domain.schema.responsabilidadeSchema import ResponsabilidadeCreate


def get_responsabilidades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Responsabilidade).offset(skip).limit(limit).all()


def create_responsabilidade(db: Session, responsabilidade: ResponsabilidadeCreate) -> Responsabilidade:
    db_responsabilidade = Responsabilidade(**responsabilidade.dict())
    db.add(db_responsabilidade)
    db.commit()
    db.refresh(db_responsabilidade)
    return db_responsabilidade



def get_responsabilidade(db: Session, responsabilidade: str):
    return db.query(Responsabilidade).filter(Responsabilidade.nome == responsabilidade).first()


def insert_permissoes_responsabilidade(db: Session, permissao_id: int, responsabilidade_id: int):

    db_responsabilidade_permissao = ResponsabilidadePermissao(
                                                                responsabilidade_id=responsabilidade_id,
                                                                permissao_id=permissao_id
                                                            )
    db.add(db_responsabilidade_permissao)
    db.commit()
    db.refresh(db_responsabilidade_permissao)

    return dict(detail="Permissão associada à Responsabilidade com sucesso!")