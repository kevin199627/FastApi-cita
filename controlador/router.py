from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from repositorio.user_schema import UserSchema, DataUser
from config.db import engine
from modelo.users import users
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List

user= APIRouter()

@user.get("/")
def root():
    return{"message:" "kevin"}

@user.get("/api/user", response_model=List[UserSchema])
def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()
        return result
    
@user.get("/api/user/{user_id}", response_model=UserSchema)
def get_user(user_id:str):
    with engine.connect() as conn:
        result = conn.execute(user.select().where(user.c.id == user_id)).first()

        return result
    

@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    with engine.connect() as conn:
    
        new_user = data_user.dict()
        new_user["contraseña"]= generate_password_hash(data_user.contraseña, "pbkdf2:sha256:30", 30)
    
        conn.execute(users.insert().values(new_user))

        return Response(status_code=HTTP_201_CREATED)
    
@user.post("/api/user/login", status_code=200)
def user_login(data_user: DataUser):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.usuario == data_user.usuario)).first()
        if result != None:
            check_passw = check_password_hash(result[3], data_user.contraseña)

            if check_passw:
                return {
                    "status": 200,
                    "message": "Access success"
                }
        
        return {
            "status": HTTP_401_UNAUTHORIZED,
            "mensage": "Access denied"
        }
            


@user.put("/api/user/{user_id}", response_model=UserSchema)
def update_user(data_update: UserSchema, user_id: str):
    with engine.connect() as conn:
        encryp_contra = generate_password_hash(data_update.contraseña,"pdbkdf2.sha256:30", 30)
        conn.execute(users.update().values(nombre=data_update.nombre, 
        apellido=data_update.apellido, usuario=data_update.usuario, contraseña=encryp_contra).where(users.c.id == user_id),
        cedula=data_update.cedula, telefono=data_update.telefono, direccion=data_update.direccion,
        correo=data_update.correo)

        result = conn.execute(users.select().where(users.c.id == user_id)).first()

        return result
    
@user.delete("/api/user/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    with engine.connect() as conn:
        conn.execute(user.delete().where(user.c.id == user_id))

        return Response(status_code=HTTP_204_NO_CONTENT)

