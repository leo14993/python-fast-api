from main import app
from fastapi import Depends
from src.bootloader.database.configuration.database import get_db
from src.domain.repository.pessoaFisicaRepository import *
from src.domain.schema.eventosPessoaSchema import EventosPessoaCreate
from src.domain.schema.pessoaFisicaSchema import PessoaFisicaCPF
from src.domain.service.eventosPessoaService import EventoPessoaService


@app.get("/pessoa/evento")
def get_evento_cpf(pessoa: PessoaFisicaCPF, db: Session = Depends(get_db)):
    evento_service = EventoPessoaService(db)
    return evento_service.get(pessoa)


@app.post("/pessoa/evento", status_code=201)
def create_evento_cpf(pessoa: EventosPessoaCreate, db: Session = Depends(get_db)):
    evento_service = EventoPessoaService(db)
    return evento_service.create(pessoa)


@app.put("/pessoa/evento", status_code=201)
def edit_evento_cpf(pessoa: EventosPessoaCreate, db: Session = Depends(get_db)):
    evento_service = EventoPessoaService(db)
    return evento_service.update(pessoa)
