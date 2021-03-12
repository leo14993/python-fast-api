from fastapi import FastAPI

app = FastAPI()

from src.domain.controller.EnderecoController import *
from src.domain.controller.PessoaFisicaController import *

