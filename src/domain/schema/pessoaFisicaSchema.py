from typing import List, Optional

from pydantic import BaseModel

from src.domain.schema.enderecoSchema import Endereco


class PessoaFisicaCPF(BaseModel):

    cpf: str

class PessoaFisicaBase(PessoaFisicaCPF):
    nome: str
    # nascimento: str
    # ToDo:
    #  acertar a forma de retornar um dado no tipo Date
    #:ToDo


class PessoaFisicaCreate(PessoaFisicaBase):
    endereco_id: int
    #Todo:
    # criar busca do endereço informado,
    # caso necessario aproveitar o endereco_id,
    # caso o endereco seja novo, criar um endereco_id
    #:ToDo


class PessoaFisica(PessoaFisicaBase):

    endereco: Endereco

    class Config:
        orm_mode = True
