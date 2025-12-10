from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from auth_users import User, auth_users
from db.models import team
from db.client import db_client
from db.schemas import team_schema


from bson import ObjectId

router = APIRouter(prefix="/usersdb", tags=["usersdb"])



# la siguiente lista pretende simular una base de datos para probar nuestra API
teams_list = []

@router.get("/", response_model=list[team.Team])
async def teams():
    # El método find() sin parámetros devuelve todos los registros
    # de la base de datos
    return team.teams_schema(db_client.test.teams.find())

# Método get tipo query. Sólo busca por id
@router.get("", response_model=team.Team)
async def team(id: str):
    return search_team_id(id)


# Método get por id
@router.get("/{id}", response_model=team.Team)
async def team(id: str):
    return search_team_id(id)


@router.post("/", response_model=team.Team, status_code=201)
async def add_team(team: team.Team):
    #print("dentro de post")
    if type(search_team(team.name, team.surname)) == team.Team:
        raise HTTPException(status_code=409, detail="Team already exists")
    
    team_dict = team.model_dump()
    del team_dict["id"]
    # Añadimos el usuario a nuestra base de datos
    # También podemos obtner con inserted_id el id que la base de datos
    # ha generado para nuestro usuario
    id= db_client.test.teams.insert_one(team_dict).inserted_id
    # Añadimos el campo id a nuestro diccionario. Hay que hacerle un cast
    # a string puesto que el id en base de datos se almacena como un objeto,
    # no como un string
    team_dict["id"] = str(id)
    # La respuesta de nuestro método es el propio usuario añadido
    # Creamos un objeto de tipo User a partir del diccionario user_dict
    return team.Team(**team_dict)
    
@router.put("/{id}", response_model=team.Team)
async def modify_team(id: str, new_team: team.Team):
    # Convertimos el usuario a un diccionario
    team_dict = new_team.model_dump()
    # Eliminamos el id en caso de que venga porque no puede cambiar
    del team_dict["id"]   
    try:
        # Buscamos el id en la base de datos y le pasamos el diccionario con los datos
        # a modificar del usuario
        db_client.test.teams.find_one_and_replace({"_id":ObjectId(id)}, team_dict)
        # Buscamos el objeto en base de datos y lo retornamos, así comprobamos que efectivamente
        # se ha modificado
        return search_team_id(id)    
    except:
        raise HTTPException(status_code=404, detail="Team not found")
    

@router.delete("/{id}", response_model=team.Team)
async def delete_team(id:str):
    found = db_client.test.teams.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Team not found")
    return team.Team(**team_schema(found))
   
# El id de la base de datos es un string, ya no es un entero
def search_team_id(id: str):    
    # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
    # así que la controlamos
    try:
        # El id en base de datos no se guarda como un string, sino que es un objeto 
        # Realizamos la conversión    
        team = team_schema(db_client.test.teams.find_one({"_id":ObjectId(id)}))
        # Necesitamos convertirlo a un objeto User. 
        return team.Team(**team)
    except:
        return {"error": "Team not found"}


def search_team(name: str, surname: str):
    # La búsqueda me devuelve un objeto del tipo de la base de datos.
    # Necesitamos convertirlo a un objeto User. 
    try:
        # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
        # así que la controlamos
        team = team_schema(db_client.test.teams.find_one({"name":name, "surname":surname}))
        return team.Team(**team)
    except:
        return {"error": "Team not found"}


def next_id():
    # Calculamos el usuario con el id más alto 
    # y le sumamos 1 a su id
    return (max(team.id for team in teams_list))+1