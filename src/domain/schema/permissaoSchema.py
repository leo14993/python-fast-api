from pydantic import BaseModel


class PermissaoBase(BaseModel):

    nome: str


class PermissaoCreate(PermissaoBase):

    descricao: str


class PermissaoSchema(PermissaoCreate):


    class Config:
        orm_mode = True