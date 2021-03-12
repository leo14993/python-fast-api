from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from src.bootloader.database.configuration.database import Base


class PessoaFisica(Base):
    __tablename__ = 'pessoa_fisica'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    cpf = Column(String(11))
    nascimento = Column(Date)
    endereco_id = Column(Integer, ForeignKey('enderecos.id'))

    endereco = relationship("Endereco", back_populates="pessoa_fisica")
