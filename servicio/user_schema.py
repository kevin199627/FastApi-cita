from pydantic import BaseModel
from typing import Optional
class UserSchema(BaseModel):
    id: Optional[str]
    nombre: str
    apellido: str
    usuario: str
    contraseña: str
    cedula: str
    telefono: str
    direccion: str
    correo: str

class DataUser(BaseModel):
    usuario: str
    contraseña: str