from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Team(BaseModel):
    id: int
    name: str
    city: str
    year_founded: int
    stadium: str

team_list = [
    Team(id=1, name="Real Betis", city="Sevilla", year_founded=1907, stadium="Benito Villamarín"),
    Team(id=2, name="FC Barcelona", city="Barcelona", year_founded=1899, stadium="Camp Nou"),
    Team(id=3, name="Real Madrid", city="Madrid", year_founded=1902, stadium="Santiago Bernabéu"),
]

@app.get("/teams")   
def teams():
    return team_list

@app.get("/teams/{id_team}")
def get_team(id_team: int):
    
    teams = [team for team in team_list if team.id == id_team]

    if len(teams) != 0:
        return teams[0]
    else:
        return {"error": "Team not found"}