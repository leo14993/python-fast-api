from fastapi import HTTPException

from src.domain.repository.permissaoRepository import permissao_exist, create_permissao
from src.domain.repository.responsabilidadeRepository import get_responsabilidade, insert_permissoes_responsabilidade
from src.domain.repository.usuarioRepository import get_usuarios
from src.domain.schema.responsabilidadeSchema import ResponsabilidadePermissao


class AuthService:
    def __init__(self, db):
        self.db = db

    def create_responsabilidade_permissao(self, responsabilidade_permissao: ResponsabilidadePermissao):
        responsabilidade_valid = get_responsabilidade(db=self.db, responsabilidade=responsabilidade_permissao.nome)
        if responsabilidade_valid:
            responsabilidade_id = responsabilidade_valid.id
            permissao_valid = permissao_exist(db=self.db, permissao=responsabilidade_permissao.permissao)
            if not permissao_valid:
                print("permissao nao existe, criando uma")
                permissao_valid = create_permissao(db=self.db, permissao=responsabilidade_permissao.permissao)

            permissao_id = permissao_valid.id

            return insert_permissoes_responsabilidade(db=self.db, permissao_id=permissao_id, responsabilidade_id=responsabilidade_id)
        else:
            raise HTTPException(status_code=400, detail="Autoridade não cadastrada na base")


    def get_usuarios(self):
        return get_usuarios(db=self.db)