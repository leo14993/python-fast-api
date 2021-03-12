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

    class Config:
        orm_mode = True

