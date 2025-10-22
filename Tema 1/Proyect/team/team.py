from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#Crear la aplicacion FastAPI
app = FastAPI()

#Clase Equipo
class Team(BaseModel):
    id: int
    name: str
    city: str
    year_founded: int
    stadium: str

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

def next_id():
    return (max(team_list, key = id).id+1)

#Metodo get para obtener todos los equipos
@app.get("/teams")   
def teams():
    return team_list


#Metodo get para obtener el equipo por su ID
@app.get("/teams/{id_team}")
def get_team_by_id(id_team: int):
    
    teams = [team for team in team_list if team.id == id_team]

    if len(teams) != 0:
        return teams[0]
    else:
        return {"error": "Team not found by ID"}


#Metodo get para obtener los equipos por su nombre
@app.get("/teams/name/{team_name}")
def get_team_by_name(team_name: str):

    teams = [team for team in team_list if team.name.lower() == team_name.lower()]

    if len(teams) != 0:
        return teams
    else:
        return {"error": "Teams not found by name"}


#Metodo get para obtener los equipos por su ciudad
@app.get("/teams/city/{city_name}")
def get_teams_by_city(city_name: str):

    teams = [team for team in team_list if team.city.lower() == city_name.lower()]
    
    if len(teams) != 0:
        return teams
    else:
        return {"error": "Teams not found by city name"}


#Metodo get para obtener los equipos por su año de fundacion
@app.get("/teams/year/{year_founded}")
def get_teams_by_year(year_founded: int):

    teams = [team for team in team_list if team.year_founded == year_founded]

    if len(teams) != 0:
        return teams
    else:
        return {"error": "Teams not found by year of foundation"}


#Metodo get para obtener los equipos por su estadio
@app.get("/teams/stadium/{stadium_name}")
def get_teams_by_stadium(stadium_name: str):

    teams = [team for team in team_list if team.stadium.lower() == stadium_name.lower()]
    
    if len(teams) != 0:
        return teams
    else:
        return {"error": "Teams not found by stadium name"}

#Metodo post para añadir un nuevo equipo
@app.post("/teams", status_code = 201, response_model = Team)
def add_team(team : Team):

    team.id = next_id()

    team_list.append(team)

    return team

@app.put("/teams/{id_team}", response_model = Team)
def modify_team_id(id: int, team: Team):
    for index, saved_team in enumerate(team_list):
        if saved_team.id == id:
            team.id = id
            team_list[index] = team
            return team
        
    raise HTTPException(status_code = 404, detail = "Team not found")

@app.put ("/teams/name/{team_name}", response_model = Team)
def modify_team_name(id: int, name: str, team = Team):
    for index, saved_team in enumerate(team_list):
        if saved_team.id == id:
            team.name = name
            team_list[index] = team
            return team
        
    raise HTTPException(status_code = 404, detail = "Team not found")

@app.put ("/teams/city/{city_name}", response_model = Team)
def modify_team_city(id: int, city: str, team = Team):
    for index, saved_team in enumerate(team_list):
        if saved_team.id == id:
            team.city = city
            team_list[index] = team
            return team
        
    raise HTTPException(status_code = 404, detail = "Team not found")

@app.put ("/teams/year/{year_founded}", response_model = Team)
def modify_team_year(id: int, year_founded: int, team = Team):
    for index, saved_team in enumerate(team_list):
        if saved_team.id == id:
            team.year_founded == year_founded
            team_list[index] = team
            return team
        
    raise HTTPException(status_code = 404, detail = "Team not found")

@app.put ("/teams/stadium/{stadium_name}", response_model = Team)
def modify_team_stadium(id: int, stadium: str, team = Team):
    for index, saved_team in enumerate(team_list):
        if saved_team.id == id:
            team.stadium == stadium
            team_list[index] = team
            return team
    
    raise HTTPException(status_code = 404, detail = "Team not found")

@app.delete("teams/{id_team}")
def delete_team(id: int):
    for saved_team in team_list:
        if saved_team.id == id:
            team_list.remove(saved_team)
            return {}
        
    raise HTTPException(status_code = 404, detail = "Team not found")