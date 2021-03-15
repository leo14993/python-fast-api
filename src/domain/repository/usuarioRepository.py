from sqlalchemy import or_
from sqlalchemy.orm import Session

from src.domain.entity.usuario import Usuario
from src.domain.schema.usuarioSchema import UsuarioCreate


def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()


def get_usuario_by_login(db: Session, login: str):
    return db.query(Usuario).filter(Usuario.login.like(login)).first()

def chek_add_usuario_by_login_email(db: Session, login: str, email: str):
    return db.query(Usuario).filter(or_(
        Usuario.login.like(login),
        Usuario.email.like(email)
        )
    ).first()


def add_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario




def edit_pessoa(db: Session, pessoa: UsuarioCreate):
    db_pessoa = Usuario(**pessoa.dict())
    db.query(Usuario).filter(Usuario.cpf == pessoa.cpf).update(pessoa.dict())
    db.commit()
    return db_pessoa


def delete_pessoa(db: Session, pessoa: UsuarioCreate):
    db_pessoa = Usuario(**pessoa.dict())
    db.query(Usuario).filter(Usuario.cpf == pessoa.cpf).delete(synchronize_session=False)
    db.commit()
    return "deletado"

# def block_usuario(db: Session, pessoa: UsuarioCreate):
