from sqlalchemy import Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from src.bootloader.database.configuration.database import Base


class PessoaEndereco(Base):
    __tablename__ = 'pessoa_endereco'
    pessoa_id = Column(Integer, ForeignKey('pessoa_fisica.id'), primary_key=True)
    endereco_id = Column(Integer, ForeignKey('enderecos.id'), primary_key=True)
    #ToDo:
    # Criar relacionamento unique together entre pessoa_id e endereco_id para evitar duplicidades no banco
    #:ToDo


class PessoaFisica(Base):
    __tablename__ = 'pessoa_fisica'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    cpf = Column(String(11), unique=True)
    data_nascimento = Column(Date)

    enderecos = relationship(
        "Endereco",
        secondary=PessoaEndereco.__tablename__,
        back_populates="pessoa_fisica",
        cascade="all, delete"
    )

    # ToDo:
    # validar campos de cpf para inserir exatamente 11 caracteres do tipo int
    #:ToDo
