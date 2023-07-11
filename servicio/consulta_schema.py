from pydantic import BaseModel
from typing import Optional
class ConsultaSchema(BaseModel):
    id: Optional[str]
    diagnostico: str
    