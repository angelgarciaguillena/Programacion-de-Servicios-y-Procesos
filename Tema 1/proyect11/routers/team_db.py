from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.models.team import Team
from db.client import db_client
from db.schemas.team import team_schema, teams_schema

from bson import ObjectId

router = APIRouter(prefix="/teamsdb", tags=["teamsdb"])

teams_list = []


@router.get("/", response_model = list[Team])
async def teams():
    return teams_schema(db_client.test.teams.find())


@router.get("/{id}", response_model=Team)
async def team(id: str):
    return search_team_id(id)


@router.post("/", response_model=Team, status_code=201)
async def add_team(team: Team):
    if type(search_team(team.name)) == Team:
        raise HTTPException(status_code=409, detail="Team already exists")
    
    team_dict = team.model_dump()
    del team_dict["id"]

    id= db_client.test.teams.insert_one(team_dict).inserted_id

    team_dict["id"] = str(id)

    return Team(**team_dict)
    

@router.put("/{id}", response_model=Team)
async def modify_team(id: str, new_team: Team):
    
    team_dict = new_team.model_dump()

    del team_dict["id"]   

    updated = db_client.test.teams.find_one_and_replace({"_id": ObjectId(id)}, team_dict)

    if not updated:
        raise HTTPException(status_code=404, detail="Team not found")

    return search_team_id(id)
    """
    Sale Interno Server Error 500 con esta forma
    try:
        
        db_client.test.teams.find_one_and_replace({"_id":ObjectId(id)}, team_dict)

        return search_team_id(id)    
    except:
        raise HTTPException(status_code=404, detail="Team not found")"""
    
    
@router.delete("/{id}", response_model=Team)
async def delete_team(id:str):
    found = db_client.test.teams.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Team not found")
    return Team(**team_schema(found))
   

def search_team_id(id: str):    
    
    team_data = db_client.test.teams.find_one({"_id": ObjectId(id)})

    if not team_data:
        raise HTTPException(status_code=404, detail="Team not found")
    
    team = team_schema(team_data)

    return Team(**team)

    """
    Devuelve Internal Server Error 500 con esta forma
    try:
        team = team_schema(db_client.test.teams.find_one({"_id":ObjectId(id)}))
        return Team(**team)
    except:
        return {"error": "Team not found"}"""


def search_team(name: str):
    try:
        team = team_schema(db_client.test.teams.find_one({"name":name}))
        return Team(**team)
    except:
        return {"error": "Team not found"}


def next_id():
    return (max(team.id for team in teams_list))+1