from typing import Optional


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

class EnderecoSchema(EnderecoBase):
    class Config:
        orm_mode = True

