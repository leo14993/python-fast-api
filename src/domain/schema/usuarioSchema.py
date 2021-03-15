from typing import List

from pydantic import BaseModel

from src.domain.schema.responsabilidadeSchema import ResponsabilidadeSchema


class UsuarioBase(BaseModel):

    login: str

class UsuarioResponsabilidade(UsuarioBase):

    responsabilidade: ResponsabilidadeSchema

class UsuarioAtivo(UsuarioBase):

    ativo: bool


class UsuarioCreate(UsuarioBase):
    senha: str


class UsuarioSchema(UsuarioAtivo):

    email: str
    responsabilidade: List[ResponsabilidadeSchema] = []

    class Config:
        orm_mode = True