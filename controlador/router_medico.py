from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from repositorio.medico_schema import MedicoSchema
from config.db import engine
from modelo.medico import medico
#from werkzeug.security import generate_password_hash, check_password_hash
from typing import List

medico= APIRouter()

@medico.get("/")
def root():
    return{ "kevin"}

@medico.get("/api/medico", response_model=List[MedicoSchema])
def get_medico():
    with engine.connect() as conn:
        result = conn.execute(medico.select()).fetchall()
        return result
    
@medico.get("/api/medico/{medico_id}", response_model=MedicoSchema)
def get_medico(medico_id:str):
    with engine.connect() as conn:
        result = conn.execute(medico.select().where(medico.c.id == medico_id)).first()

        return result

@medico.post("/api/medico", status_code=HTTP_201_CREATED)
def create_medico(data_medico: MedicoSchema):
    with engine.connect() as conn:
    
        new_medico = data_medico.dict()
        #new_medico["contraseña"]= generate_password_hash(data_user.contraseña, "pbkdf2:sha256:30", 30)
    
        conn.execute(medico.insert().values(new_medico))

        return Response(status_code=HTTP_201_CREATED)
    

@medico.put("/api/medico/{medico_id}", response_model=MedicoSchema)
def update_medico(data_update: MedicoSchema, medico_id: str):
    with engine.connect() as conn:
        #encryp_contra = generate_password_hash(data_update.contraseña,"pdbkdf2.sha256:30", 30)
        conn.execute(medico.update().values(nombre=data_update.nombre, 
        apellido=data_update.apellido, especialidad=data_update.especialidad,
        cedula=data_update.cedula, telefono=data_update.telefono))

        result = conn.execute(medico.select().where(medico.c.id == medico_id)).first()

        return result
    

@medico.delete("/api/medico/{medico_id}", status_code=HTTP_204_NO_CONTENT)
def delete_medico(medico_id: str):
    with engine.connect() as conn:
        conn.execute(medico.delete().where(medico.c.id == medico_id))

        return Response(status_code=HTTP_204_NO_CONTENT)