from typing import Optional
from pydantic import BaseModel
    
#Clase Equipo
class Team(BaseModel):
    id: Optional[str] #Id del equipo
    name: str #Nombre del equipo
    city: str #Ciudad del equipo
    year_founded: int #Año de fundacion del equipo
    stadium: str #Estadio del equipo   