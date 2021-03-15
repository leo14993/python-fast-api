import base64
from datetime import datetime, timedelta

import bcrypt
from fastapi import HTTPException
from sqlalchemy.util import raise_

from src.domain.entity.usuario import Usuario
from src.domain.repository.permissaoRepository import permissao_exist, create_permissao
from src.domain.repository.responsabilidadeRepository import get_responsabilidade, insert_permissoes_responsabilidade
from src.domain.repository.usuarioRepository import get_usuarios, get_usuario_by_login, add_usuario, \
    chek_add_usuario_by_login_email
from src.domain.schema.responsabilidadeSchema import ResponsabilidadePermissao



class AuthService:
    def __init__(self, db):
        self.db = db
        self.not_exist = type(None)
        self.valida_senha = lambda senha_digitada, hash_senha: raise_(
            HTTPException(
                status_code=401,
                detail="Usuário/Senha incorretos!")
        ) if not bcrypt.hashpw(senha_digitada, hash_senha) == hash_senha else True


    def check_user_create(self,login: str, email: str ):
        usuario = chek_add_usuario_by_login_email(self.db, login=login, email=email)
        if not isinstance(usuario, self.not_exist):
            raise HTTPException(
                status_code=403,
                detail="Não é possível Criar. Já existe um usuário com o mesmo login/email.")
        else:
            return True

    def check_user_login(self,login: str, email: str ):
        usuario = chek_add_usuario_by_login_email(self.db, login=login, email=email)
        if isinstance(usuario, self.not_exist):
            raise HTTPException(
                status_code=404,
                detail="Não é possível logar. O usuário não existe!")
        else:
            return usuario

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
            raise HTTPException(status_code=404, detail="Autoridade não cadastrada na base")


    def get_usuarios(self):
        return get_usuarios(db=self.db)

    def get_usuario(self, login: str):
        usuario = get_usuario_by_login(db=self.db, login=login)
        if usuario:
            return get_usuario_by_login(db=self.db, login=login)
        else:
            raise HTTPException(status_code=404, detail="Usuário não cadastrado na base")


    #ToDo:
    # salvar token de usuario na sessao
    # salvar permissoes de usuario na sessao
    #:ToDo

    def create_usuario(self, usuario: Usuario):
        usuario_valido = self.check_user_create(login=usuario.login, email=usuario.email)
        if usuario_valido:
            print(usuario_valido)
            usuario.senha = bcrypt.hashpw(usuario.senha, bcrypt.gensalt())
            return add_usuario(db=self.db, usuario=usuario)
        else:
            print(usuario_valido)
            raise HTTPException(status_code=400, detail="Usuário já cadastrado na base")


    def login(self, usuario: Usuario):
        usuario_valido = self.check_user_login(login=usuario.login, email=usuario.email)
        self.valida_senha(usuario.senha, usuario_valido.senha)
        token = base64.b64encode(
            bytes(bcrypt.hashpw("P3r0laNegr@", bcrypt.gensalt()), 'utf-8')).decode("utf-8")
        token_expira = timedelta(hours=2) + datetime.now()
        return dict(token=token, token_validate=token_expira)

    # ToDo:
    # Criar funcionalidade para bloquear usuario
    #:ToDo
    def bloquear_usuario(self):
        pass


