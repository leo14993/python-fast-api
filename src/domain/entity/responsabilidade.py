from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from src.bootloader.database.configuration.database import Base


class ResponsabilidadePermissao(Base):
    __tablename__ = 'responsabilidades_permissoes'
    permissao_id = Column(Integer, ForeignKey('permissoes.id'), primary_key=True)
    responsabilidade_id = Column(Integer, ForeignKey('responsabilidades.id'), primary_key=True)
    # ToDo:
    # Criar relacionamento unique together entre permissao_id e responsabilidade_id para evitar duplicidades no banco
    #:ToDo

class ResponsabilidadeUsuario(Base):
    __tablename__ = 'responsabilidades_usuarios'
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    responsabilidade_id = Column(Integer, ForeignKey('responsabilidades.id'), primary_key=True)
    # ToDo:
    # Criar relacionamento unique together entre permissao_id e responsabilidade_id para evitar duplicidades no banco
    #:ToDo

class Responsabilidade(Base):
    __tablename__ = 'responsabilidades'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), unique=True)
    permissoes = relationship(
        "Permissao",
        secondary=ResponsabilidadePermissao.__tablename__,
        back_populates="responsabilidade",
        cascade="all, delete"
    )
    usuarios = relationship(
        "Usuario",
        secondary=ResponsabilidadeUsuario.__tablename__,
        back_populates="responsabilidade",
        cascade="all, delete"
    )
