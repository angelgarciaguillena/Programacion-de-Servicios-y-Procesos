from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

#Crear la aplicacion FastAPI
router = APIRouter(prefix="/teams", tags=["teams"])

#Clase Equipo
class Team(BaseModel):
    id: int #Id del equipo
    name: str #Nombre del equipo
    city: str #Ciudad del equipo
    year_founded: int #Año de fundacion del equipo
    stadium: str #Estadio del equipo


#Lista de equipos de ejemplo
team_list = [
    Team(id=1, name="Real Betis", city="Sevilla", year_founded=1907, stadium="Benito Villamarín"),
    Team(id=2, name="FC Barcelona", city="Barcelona", year_founded=1899, stadium="Camp Nou"),
    Team(id=3, name="Real Madrid", city="Madrid", year_founded=1902, stadium="Santiago Bernabéu"),
    Team(id=4, name="Atlético de Madrid", city="Madrid", year_founded=1903, stadium="Wanda Metropolitano"),
    Team(id=5, name="Sevilla FC", city="Sevilla", year_founded=1890, stadium="Ramón Sánchez Pizjuán"),
    Team(id=6, name="Valencia CF", city="Valencia", year_founded=1919, stadium="Mestalla"),
    Team(id=7, name="Villarreal CF", city="Villarreal", year_founded=1923, stadium="Estadio de la Cerámica"),
    Team(id=8, name="Athletic Club", city="Bilbao", year_founded=1898, stadium="San Mamés"),
    Team(id=9, name="Real Sociedad", city="San Sebastián", year_founded=1909, stadium="Anoeta"),
    Team(id=10, name="Celta de Vigo", city="Vigo", year_founded=1923, stadium="Balaídos"),
]


#Funcion para obtener el siguiente ID disponible
def next_id():
    return (max(team_list, key = id).id+1)


def search_team(id: int):
    #teams = filter(lambda team: team.id==id, team_list)
    return [team for team in team_list if team.id == id]


#region Metodos get
#Metodo get para obtener todos los equipos
@router.get("/")   
def teams():
    return team_list


#Metodo get para obtener el equipo por su ID
@router.get("/{id_team}")
def get_team_by_id(id_team: int):

    #Buscamos el equipo por su ID y lo almacenamos en una lista
    teams = search_team(id_team)

    #Si encontramos al equipo lo devolvemos
    if len(teams) != 0:
        return teams[0]
    
    #Si no encontramos al equipo devolvemos un mensaje de error
    else:
        raise HTTPException(status_code=404, detail="Team not found")
#endregion


#region Metodos post
#Metodo post para añadir un nuevo equipo
@router.post("/", status_code = 201, response_model = Team)
def add_team(team : Team):
    
    #Llamamos a la funcion para asignar un ID al nuevo equipo
    team.id = next_id()

    #Añadimos el nuevo equipo a la lista de equipos
    team_list.append(team)

    #Devolvemos el equipo que se ha añadido
    return team
#endregion

#region Metodos put
#Metodo put para modificar un equipo existente
@router.put("/{id_team}", response_model = Team)
def modify_team(id_team: int, team: Team):

    #Creamos un bucle for para recorrer la lista de equipos
    for index, saved_team in enumerate(team_list):

        #Si el id del equipo es igual al id que queremos modificar, modificamos el equipo
        if saved_team.id == id_team:

            #Asignamos el ID al equipo modificado
            team.id = id_team

            #Actualizamos el equipo en la lista de equipos
            team_list[index] = team

            #Devolvemos el equipo que se ha modificado
            return team

    #Si no encontramos el equipo devolvemos un mensaje de error 
    raise HTTPException(status_code = 404, detail = "Team not found")
#endregion

#region Metodos delete
#Metodo delete para eliminar un equipo existente
@router.delete("/{id_team}")
def delete_team(id_team: int):

    #Creamos un bucle for para recorrer la lista de equipos
    for saved_team in team_list:

        #Si el id del equipo es igual al id que queremos eliminar, eliminamos el equipo
        if saved_team.id == id_team:

            #Eliminamos el equipo de la lista de equipos
            team_list.remove(saved_team)

            #Devolvemos un diccionario vacio
            return {}

    #Si no encontramos el equipo devolvemos un mensaje de error
    raise HTTPException(status_code = 404, detail = "Team not found")
#endregion