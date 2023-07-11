from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from repositorio.cita_schema import CitaSchema
from config.db import engine
from modelo.citas import citas
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List

cita= APIRouter()


@cita.post("/api/cita", status_code=HTTP_201_CREATED)
def create_cita(data_cita: CitaSchema):
    with engine.connect() as conn:
    
        new_cita = data_cita.dict()
    
        conn.execute(citas.insert().values(new_cita))

        return Response(status_code=HTTP_201_CREATED)
    

@cita.put("/api/cita/{cita_id}", response_model=CitaSchema)
def update_cita(data_update: CitaSchema, cita_id: str):
    with engine.connect() as conn:
        conn.execute(citas.update().values(fecha=data_update.fecha, 
        hora=data_update.hora, estado=data_update.estado))

        result = conn.execute(citas.select().where(citas.c.id == cita_id)).first()

        return result
    

@cita.delete("/api/cita/{cita_id}", status_code=HTTP_204_NO_CONTENT)
def delete_cita(cita_id: str):
    with engine.connect() as conn:
        conn.execute(cita.delete().where(cita.c.id == cita_id))

        return Response(status_code=HTTP_204_NO_CONTENT)