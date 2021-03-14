from datetime import date
from typing import List

from pydantic import BaseModel

from src.domain.schema.enderecoSchema import EnderecoSchema


class PessoaFisicaCPF(BaseModel):

    cpf: str

class PessoaFisicaEndereco(PessoaFisicaCPF):

    enderecos: EnderecoSchema

class PessoaFisicaBase(PessoaFisicaCPF):
    nome: str
    data_nascimento: date = None
    class Config:
        orm_mode = True


class PessoaFisicaCreate(PessoaFisicaBase):

    pass

class PessoaFisicaSchema(PessoaFisicaBase):
    enderecos: List[EnderecoSchema] = []
    class Config:
        orm_mode = True
