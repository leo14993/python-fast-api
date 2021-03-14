from fastapi import HTTPException

from src.domain.repository.enderecoRepository import endereco_exist, create_endereco
from src.domain.repository.pessoaFisicaRepository import get_pessoas, get_pessoa_by_cpf, create_pessoa, edit_pessoa, \
    delete_pessoa, add_endereco_pessoa, cpf_exists
from src.domain.schema.pessoaFisicaSchema import PessoaFisicaEndereco


def raise_(exception):
    raise exception

class PessoaService():
    def __init__(self, db):

        super().__init__(db)
        self.db = db
        self.skip = 0
        self.limit = 100
        self.not_exist = type(None)
        self.get_function = lambda cpf: get_pessoa_by_cpf(db=self.db, cpf=cpf)
        self.get_all_function = lambda: get_pessoas(db=self.db, skip=self.skip, limit=self.limit)
        self.check_cpf_update = lambda cpf: raise_(
            HTTPException(
                status_code=400,
                detail="Não é possível Exluir/Alterar. O CPF informado não existe na base")
        ) if isinstance(cpf_exists(self.db, cpf=cpf), self.not_exist) else True

        self.check_cpf_create = lambda cpf: raise_(
            HTTPException(
                status_code=400,
                detail="Não é possível Criar. O CPF informado já existe na base")
        ) if not isinstance(cpf_exists(self.db, cpf=cpf), self.not_exist) else True


    def get_all(self):
        print(self.limit)
        return get_pessoas(db=self.db, skip=self.skip, limit=self.limit)

    def get(self, pessoa):
        pessoa_exist = self.check_cpf_update(pessoa.cpf)
        if pessoa_exist:
            return self.get_function(pessoa.cpf)
        else:
            raise HTTPException(status_code=400, detail="Sem informações para este CPF")


    def create(self, pessoa):
        evento_exist = self.check_cpf_create(pessoa.cpf)
        if evento_exist:
            return create_pessoa(db=self.db, pessoa=pessoa)


    def update(self, pessoa):
        evento_exist = self.check_cpf_update(pessoa.cpf)
        if evento_exist:
            return edit_pessoa(db=self.db, pessoa=pessoa)
        else:
            raise HTTPException(status_code=400, detail="CPF não cadastrado na base")

    def delete(self, pessoa):
        evento_exist = self.check_cpf_update(pessoa.cpf)
        if evento_exist:
            return delete_pessoa(db=self.db, pessoa=pessoa)
        else:
            raise HTTPException(status_code=400, detail="CPF não cadastrado na base")

    def create_endereco_pessoa(self, pessoa: PessoaFisicaEndereco):
        get_pessoa = get_pessoa_by_cpf(db=self.db, cpf=pessoa.cpf)
        if get_pessoa:
            pessoa_id = get_pessoa.id
            endereco_valid = endereco_exist(db=self.db, endereco=pessoa.enderecos)
            if endereco_valid:
                endereco_id = endereco_valid.id
            else:
                endereco_valid = create_endereco(db=self.db, endereco=pessoa.enderecos)
                endereco_id = endereco_valid.id


            return add_endereco_pessoa(db=self.db, pessoa_id=pessoa_id, endereco_id=endereco_id)

        else:
            raise HTTPException(status_code=400, detail="CPF não cadastrado na base")
