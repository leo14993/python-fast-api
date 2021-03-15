from typing import List

from pydantic import BaseModel

from src.domain.schema.permissaoSchema import PermissaoSchema


class ResponsabilidadeBase(BaseModel):

    nome: str

class ResponsabilidadeCreate(ResponsabilidadeBase):

    pass


class ResponsabilidadePermissao(ResponsabilidadeBase):

    permissao: PermissaoSchema

class ResponsabilidadeSchema(ResponsabilidadeBase):

    permissoes: List[PermissaoSchema] = []

    class Config:
        orm_mode = True