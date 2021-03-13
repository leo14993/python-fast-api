from fastapi import FastAPI


app = FastAPI()

from src.domain.controller.enderecoController import *
from src.domain.controller.pessoaFisicaController import *
from src.domain.controller.eventosPessoaController import *
from src.domain.controller.redisManagerController import *


