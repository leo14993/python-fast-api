from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.bootloader.database.configuration.database import Base
from src.domain.entity.responsabilidade import ResponsabilidadePermissao


class Permissao(Base):
    __tablename__ = 'permissoes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(512), unique=True)
    descricao = Column(String(1024))
    responsabilidade = relationship(
        "Responsabilidade",
        secondary=ResponsabilidadePermissao.__tablename__,
        back_populates="permissoes",
        cascade="all, delete"
    )

