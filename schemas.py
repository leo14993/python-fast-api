from typing import List, Optional


from pydantic import BaseModel
class EnderecoBase(BaseModel):

    cep: str
    endereco: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None

class EnderecoCreate(EnderecoBase):

    pass

class Endereco(EnderecoBase):
    id: int

    class Config:
        orm_mode = True


class PessoaFisicaBase(BaseModel):

    nome: str
    cpf: str
    # nascimento: str


class PessoaFisicaCreate(PessoaFisicaBase):

    pass


class PessoaFisica(PessoaFisicaBase):
    id: int
    # endereco: List[Endereco] = []
    endereco_id: int

    class Config:
        orm_mode = True