from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from routers import auth_users

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


#region Metodos get
#Metodo get para obtener todos los equipos
@router.get("/")   
def teams():
    return team_list


#Metodo get para obtener el equipo por su ID
@router.get("/{id_team}")
def get_team_by_id(id_team: int):

    #Buscamos el equipo por su ID y lo almacenamos en una lista
    teams = [team for team in team_list if team.id == id_team]

    #Si encontramos al equipo lo devolvemos
    if teams:
        return teams[0]
    
    #Si no encontramos al equipo devolvemos un mensaje de error
    else:
        return {"error": "Team not found by ID"}


#Metodo get para obtener los equipos por su nombre
@router.get("/name/{team_name}")
def get_team_by_name(team_name: str):

    #Buscamos los equipos por su nombre y los almacenamos en una lista
    teams = [team for team in team_list if team.name.lower() == team_name.lower()]

    #Si encontramos los equipos los devolvemos
    if teams:
        return teams

    #Si no encontramos los equipos devolvemos un mensaje de error
    else:
        return {"error": "Teams not found by name"}


#Metodo get para obtener los equipos por su ciudad
@router.get("/city/{city_name}")
def get_teams_by_city(city_name: str):

    #Buscamos los equipos por su ciudad y los almacenamos en una lista
    teams = [team for team in team_list if team.city.lower() == city_name.lower()]

    #Si encontramos los equipos los devolvemos
    if teams:
        return teams
    
    #Si no encontramos los equipos devolvemos un mensaje de error
    else:
        return {"error": "Teams not found by city name"}


#Metodo get para obtener los equipos por su año de fundacion
@router.get("/year/{year_founded}")
def get_teams_by_year(year_founded: int):

    #Buscamos los equipos por su año de fundacion y los almacenamos en una lista
    teams = [team for team in team_list if team.year_founded == year_founded]

    #Si encontramos los equipos los devolvemos
    if teams:
        return teams
    
    #Si no encontramos los equipos devolvemos un mensaje de error
    else:
        return {"error": "Teams not found by year of foundation"}


#Metodo get para obtener los equipos por su estadio
@router.get("/stadium/{stadium_name}")
def get_teams_by_stadium(stadium_name: str):

    #Buscamos los equipos por su estadio y los almacenamos en una lista
    teams = [team for team in team_list if team.stadium.lower() == stadium_name.lower()]

    #Si encontramos los equipos los devolvemos
    if teams:
        return teams
    
    #Si no encontramos los equipos devolvemos un mensaje de error
    else:
        return {"error": "Teams not found by stadium name"}
#endregion

#region Metodos post
#Metodo post para añadir un nuevo equipo
@router.post("/", status_code = 201, response_model = Team)
def add_team(team : Team, authorized = Depends(auth_users)):

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