from fastapi import HTTPException
from src.bootloader.database.configuration.redis import redis_cache
from src.domain.entity.eventosPessoa import EventosPessoa
from src.domain.repository.pessoaFisicaRepository import cpf_exists


class EventoPessoaService:
    def __init__(self, db):

        self.db = db

    def check_cpf(self, cpf):
        not_exist = type(None)
        event = redis_cache.get(key=str(cpf), serialization=True)
        if isinstance(event, not_exist):
            cpf_base = cpf_exists(self.db, cpf=cpf)
            if isinstance(cpf_base, not_exist):
                raise HTTPException(status_code=400, detail="Não é possível Criar/Alterar o evento. "
                                                            "O CPF informado não existe na base")
            return False

        return event

    def get(self, pessoa):
        event_exist = self.check_cpf(pessoa.cpf)
        if event_exist:
            return event_exist
        else:
            raise HTTPException(status_code=400, detail="Sem informações para este CPF")

    def create_update(self, pessoa):
        pessoa_create = EventosPessoa(
            cpf=pessoa.cpf,
            ultimaConsulta=pessoa.ultimaConsulta,
            movimentacaoFinanceira=pessoa.movimentacaoFinanceira,
            dadosUltimaCompra=pessoa.dadosUltimaCompra
        ).__dict__

        try:
            redis_cache.set(key=pessoa.cpf,
                            value=pessoa_create,
                            serialization=True)

            return redis_cache.get(key=str(pessoa.cpf), serialization=True)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Problemas ao salvar informações no cache. Exception: {e}")


    def create(self, pessoa):
        evento_exist = self.check_cpf(pessoa.cpf)
        if evento_exist:
            raise HTTPException(status_code=403, detail="Evento do CPF já existe!")

        return self.create_update_evento(pessoa)


    def update(self, pessoa):
        evento_exist = self.check_cpf(pessoa.cpf)
        if evento_exist:
            return self.create_update_evento(pessoa)
        else:
            raise HTTPException(status_code=400, detail="CPF não cadastrado na base")