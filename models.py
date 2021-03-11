from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from database import Base

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

    # pessoa_fisica = relationship("PessoaFisica", back_populates="endereco")


class PessoaFisica(Base):
    __tablename__ = 'pessoa_fisica'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    cpf = Column(String(11))
    nascimento = Column(Date)
    endereco_id = Column(Integer, ForeignKey('enderecos.id'))
    #
    # endereco = relationship("Endereco", back_populates="pessoa_fisica")
