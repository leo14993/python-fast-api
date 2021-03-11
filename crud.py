from sqlalchemy.orm import Session
import models, schemas
def get_enderecos(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Endereco).offset(skip).limit(limit).all()

def get_pessoas(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.PessoaFisica).offset(skip).limit(limit).all()