from typing import Union
from controlador.router import user
from fastapi import FastAPI
from controlador.router_medico import medico
from controlador.router_cita import cita
from controlador.router_consulta import consulta

app = FastAPI()

app.include_router(user)

app.include_router(medico)

app.include_router(cita)

app.include_router(consulta)

