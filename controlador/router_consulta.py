from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from repositorio.consulta_schema import ConsultaSchema
from config.db import engine
from modelo.consultas import consultas
from typing import List

consulta= APIRouter()

@consulta.post("/api/consulta", status_code=HTTP_201_CREATED)
def create_consulta(data_consulta: ConsultaSchema):
    with engine.connect() as conn:
    
        new_consulta = data_consulta.dict()
    
        conn.execute(consultas.insert().values(new_consulta))

        return Response(status_code=HTTP_201_CREATED)
    

@consulta.put("/api/consulta/{consulta_id}", response_model=ConsultaSchema)
def update_consulta(data_update: ConsultaSchema, consulta_id: str):
    with engine.connect() as conn:
        conn.execute(consultas.update().values(diagnostico=data_update.diagnostico))

        result = conn.execute(consultas.select().where(consultas.c.id == consulta_id)).first()

        return result
    

@consulta.delete("/api/consulta/{consulta_id}", status_code=HTTP_204_NO_CONTENT)
def delete_consulta(consulta_id: str):
    with engine.connect() as conn:
        conn.execute(consulta.delete().where(consulta.c.id == consulta_id))

        return Response(status_code=HTTP_204_NO_CONTENT)