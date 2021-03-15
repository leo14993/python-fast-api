from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from main import app
from src.bootloader.database.configuration.database import get_db
from src.domain.repository.permissaoRepository import create_permissao, get_permissoes
from src.domain.repository.responsabilidadeRepository import get_responsabilidades
from src.domain.schema.permissaoSchema import PermissaoCreate, PermissaoSchema
from src.domain.schema.responsabilidadeSchema import ResponsabilidadeSchema, ResponsabilidadePermissao
from src.domain.schema.usuarioSchema import UsuarioSchema, UsuarioCreate
from src.domain.service.authService import AuthService






@app.get("/permissao", response_model=List[PermissaoSchema])
def permissao(db: Session = Depends(get_db)):

    return get_permissoes(db)

@app.post("/permissao", response_model=PermissaoSchema)
def nova_permissao(permissao: PermissaoCreate, db: Session = Depends(get_db)):
    return create_permissao(db=db, permissao=permissao)

@app.get("/get_responsabilidade",response_model=List[ResponsabilidadeSchema])
def responsabilidade(db: Session = Depends(get_db)):
    responsabilidades = get_responsabilidades(db)
    return responsabilidades

@app.post("/responsabilidade/permissao", response_model=dict)
def create_responsabilidade_permissao(permissao: ResponsabilidadePermissao, db: Session = Depends(get_db)):
    responsabilidade = AuthService(db)
    return responsabilidade.create_responsabilidade_permissao(permissao)


@app.get("/usuarios", response_model=List[UsuarioSchema])
def usuarios(db: Session = Depends(get_db)):
    usuario_service = AuthService(db)
    return usuario_service.get_usuarios()

@app.get("/usuario/{login}", response_model=UsuarioSchema)
def permissao(login: str, db: Session = Depends(get_db)):
    usuario_service = AuthService(db)
    return usuario_service.get_usuario(login=login)

@app.post("/usuario", response_model=UsuarioSchema)
def novo_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_service = AuthService(db)
    return usuario_service.create_usuario(usuario=usuario)

@app.post("/login")
def login(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_service = AuthService(db)
    return usuario_service.login(usuario=usuario)

