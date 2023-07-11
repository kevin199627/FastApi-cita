from pydantic import BaseModel
from typing import Optional
class CitaSchema(BaseModel):
    id: Optional[str]
    fecha: str
    hora: str
    estado: str
    