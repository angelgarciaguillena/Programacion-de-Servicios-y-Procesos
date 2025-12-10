from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.models.player import Player
from db.client import db_client
from db.schemas.player import player_schema, players_schema

from bson import ObjectId

router = APIRouter(prefix="/playersdb", tags=["playersdb"])

players_list = []


@router.get("/", response_model = list[Player])
async def players():
    return players_schema(db_client.test.players.find())


@router.get("/{id}", response_model=Player)
async def player(id: str):
    return search_player_id(id)


@router.post("/", response_model=Player, status_code=201)
async def add_player(player: Player):
    if type(search_player(player.name)) == Player:
        raise HTTPException(status_code=409, detail="Player already exists")
    
    player_dict = player.model_dump()
    del player_dict["id"]

    id= db_client.test.players.insert_one(player_dict).inserted_id

    player_dict["id"] = str(id)
    return Player(**player_dict)
    

@router.put("/{id}", response_model=Player)
async def modify_player(id: str, new_player: Player):
    
    player_dict = new_player.model_dump()

    del player_dict["id"]   
    updated = db_client.test.players.find_one_and_replace({"_id": ObjectId(id)}, player_dict)

    if not updated:
        raise HTTPException(status_code=404, detail="Player not found")
    return search_player_id(id)
    """
    Sale Interno Server Error 500 con esta forma
    try:
        
        db_client.test.teams.find_one_and_replace({"_id":ObjectId(id)}, team_dict)

        return search_team_id(id)    
    except:
        raise HTTPException(status_code=404, detail="Team not found")"""
    
    
@router.delete("/{id}", response_model=Player)
async def delete_player(id:str):
    found = db_client.test.players.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Player not found")
    return Player(**player_schema(found))
   

def search_player_id(id: str):    
    
    player_data = db_client.test.players.find_one({"_id": ObjectId(id)})

    if not player_data:
        raise HTTPException(status_code=404, detail="Player not found")
    
    player = player_schema(player_data)

    return Player(**player)
    """
    Devuelve Internal Server Error 500 con esta forma
    try:
        team = team_schema(db_client.test.teams.find_one({"_id":ObjectId(id)}))
        return Team(**team)
    except:
        return {"error": "Team not found"}"""


def search_player(name: str):
    try:
        player = player_schema(db_client.test.players.find_one({"name":name}))
        return Player(**player)
    except:
        return {"error": "Player not found"}


def next_id():
    return (max(player.id for player in players_list))+1