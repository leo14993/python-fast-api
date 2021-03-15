from sqlalchemy.orm import Session

from src.domain.entity.usuario import Usuario
from src.domain.schema.usuarioSchema import UsuarioCreate


def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()
