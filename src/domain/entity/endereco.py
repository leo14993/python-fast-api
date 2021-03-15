from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.bootloader.database.configuration.database import Base
from src.domain.entity.pessoaFisica import PessoaEndereco


class Endereco(Base):
    __tablename__ = 'enderecos'

    id = Column(Integer, primary_key=True, index=True)
    cep = Column(String(8))
    endereco = Column(String(255))
    numero = Column(String(12))
    complemento = Column(String(255))
    bairro = Column(String(255))
    cidade = Column(String(255))
    estado = Column(String(255))
    pessoa_fisica = relationship(
        "PessoaFisica",
        secondary=PessoaEndereco.__tablename__,
        back_populates="enderecos",
        cascade="all, delete"
    )