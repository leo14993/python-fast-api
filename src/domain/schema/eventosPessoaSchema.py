from typing import List, Optional

from pydantic import BaseModel

from src.domain.schema.enderecoSchema import EnderecoSchema


class DadosUltimaCompra(BaseModel):

             valor: float
             local: str
             data: str


class EventosPessoaCreate(BaseModel):

    cpf: str
    ultimaConsulta: str
    movimentacaoFinanceira: float
    dadosUltimaCompra: DadosUltimaCompra

    class Config:
        orm_mode = True
