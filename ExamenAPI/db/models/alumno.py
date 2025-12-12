from typing import Optional
from pydantic import BaseModel

class Alumno(BaseModel):
    id: Optional[str]
    nombre: str
    apellidos: str
    fecha_nacimiento: str
    curso: str
    repetidor: bool
    id_colegio: str