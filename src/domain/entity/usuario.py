
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship

from src.bootloader.database.configuration.database import Base
from src.domain.entity.responsabilidade import ResponsabilidadeUsuario


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    login = Column(String(50), unique=True)
    senha = Column(String(255))
    email = Column(String(255), unique=True)
    ativo = Column(Boolean, default=True)
    responsabilidade = relationship(
        "Responsabilidade",
        secondary=ResponsabilidadeUsuario.__tablename__,
        back_populates="usuarios",
        cascade="all, delete"
    )

    # ToDo:
    # tratar o erro de
    # validar campos de senha num padrao seguro
    #:ToDo