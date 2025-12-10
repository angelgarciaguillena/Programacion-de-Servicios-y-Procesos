from typing import Optional
from pydantic import BaseModel
    
#Creamos la clase Jugador
class Player(BaseModel):
    id: Optional[str] #Id del jugador
    name: str #Nombre del jugador
    age: int #Edad del jugador
    position: str #Posicion del jugador
    nationality: str #Nacionalidad del jugador
    salary: float #Salario del jugador
    id_team: Optional[str] #Id del equipo al que pertenece el jugador