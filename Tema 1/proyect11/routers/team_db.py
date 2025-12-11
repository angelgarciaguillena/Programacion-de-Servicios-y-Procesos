from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.models.team import Team
from db.client import db_client
from db.schemas.team import team_schema, teams_schema

from bson import ObjectId

# APIRouter con prefijo y etiqueta para la documentación
router = APIRouter(prefix="/teamsdb", tags=["teamsdb"])

# Lista auxiliar en memoria (se utiliza sólo para la función `next_id()`)
teams_list = []


"""Devuelve la lista de todos los equipos.

        - Recupera un cursor con `find()` sobre la colección `test.teams`.
        - `teams_schema` transforma el cursor en una lista de diccionarios
            con los campos necesarios para construir los objetos `Team`.
        - Retorna `list[Team]` para que FastAPI pueda validar y documentar
            la respuesta automáticamente.
        """
@router.get("/", response_model = list[Team])
async def teams():
    return teams_schema(db_client.test.teams.find())


"""Obtiene un equipo por su `id` (string que representa un `ObjectId`).

    - `id`: cadena que representa un `ObjectId` de MongoDB.
    - Se delega en `search_team_id` que convierte y valida la existencia.
    """
@router.get("/{id}", response_model=Team)
async def team(id: str):
    return search_team_id(id)


"""Crea un nuevo equipo en la colección.

    - Valida que no exista ya un equipo con el mismo nombre (conflicto 409).
    - Convierte el modelo Pydantic a diccionario y elimina `id` para que
      MongoDB genere `_id` automáticamente.
    - Inserta el documento y devuelve el nuevo `Team` con `id` como string.
    """
@router.post("/", response_model=Team, status_code=201)
async def add_team(team: Team):
    if type(search_team(team.name)) == Team:
        raise HTTPException(status_code=409, detail="Team already exists")

    team_dict = team.model_dump()
    # Eliminar el campo id antes de insertar en MongoDB
    del team_dict["id"]

    id = db_client.test.teams.insert_one(team_dict).inserted_id

    # Convertir ObjectId a string para devolverlo en el modelo Team
    team_dict["id"] = str(id)

    return Team(**team_dict)
    

"""Actualiza un equipo existente por su `id`.

    - `new_team` es un objeto Pydantic con los datos a sustituir.
    - Eliminamos `id` del diccionario porque MongoDB identifica por `_id`.
    - `find_one_and_replace` reemplaza el documento completo.
    - Si no se encontró el documento, se lanza un 404.
    """
@router.put("/{id}", response_model=Team)
async def modify_team(id: str, new_team: Team):
    
    team_dict = new_team.model_dump()

    # No incluimos `id` en la operación sobre MongoDB
    del team_dict["id"]

    updated = db_client.test.teams.find_one_and_replace({"_id": ObjectId(id)}, team_dict)

    if not updated:
        raise HTTPException(status_code=404, detail="Team not found")

    # Devolver la versión actualizada del equipo
    return search_team_id(id)
    """
    Sale Interno Server Error 500 con esta forma
    try:
        
        db_client.test.teams.find_one_and_replace({"_id":ObjectId(id)}, team_dict)

        return search_team_id(id)    
    except:
        raise HTTPException(status_code=404, detail="Team not found")"""
    

"""Elimina un equipo por su `id` y devuelve el documento eliminado.

    - Usa `find_one_and_delete` para borrar y obtener el documento.
    - Si no existe, lanza `HTTPException(404)`.
    - Convierte el documento eliminado con `team_schema` y construye un `Team`.
    """
@router.delete("/{id}", response_model=Team)
async def delete_team(id:str):
    found = db_client.test.teams.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Team not found")
    return Team(**team_schema(found))
   

"""Busca y devuelve un equipo por su `id`.

    - Convierte el `id` en `ObjectId` y hace `find_one`.
    - Si no existe, lanza `HTTPException(404)`.
    - Convierte el documento con `team_schema` y crea un objeto `Team`.
    """
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


"""Busca un equipo por su nombre.

    - Intenta localizar el documento por el campo `name`.
    - Si se encuentra, transforma y devuelve `Team`.
    - Si ocurre cualquier error (p. ej. None), devuelve un dict con error.
    """
def search_team(name: str):
    try:
        team = team_schema(db_client.test.teams.find_one({"name": name}))
        return Team(**team)
    except:
        return {"error": "Team not found"}


"""Calcula un id siguiente a partir de `teams_list` en memoria.

        - Función auxiliar que sólo tiene sentido si `teams_list` contiene
            objetos con el atributo `id`.
        - Si `teams_list` está vacío lanzará `ValueError` al llamar a `max()`.
        - En esta aplicación real la persistencia se hace en MongoDB, por lo que
            esta función no se usa para la generación de ids persistentes.
        """
def next_id():
    return (max(team.id for team in teams_list))+1