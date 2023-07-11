from pydantic import BaseModel
from typing import Optional

class MedicoSchema(BaseModel):
    id: Optional[str]
    nombre: str
    apellido: str
    especialidad: str
    cedula: str
    telefono: str