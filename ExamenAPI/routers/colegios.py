from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.schemas.colegio import colegio_schema, colegios_schema
from db.models.colegio import Colegio
from db.client import db_client
from db.schemas.alumno import alumnos_schema
from routers.alumnos import delete_alumno

from bson import ObjectId

router = APIRouter(prefix="/colegios", tags=["colegios"])

colegios_list = []

@router.get("/", response_model = list[Colegio])
async def colegios():
    return colegios_schema(db_client.test.colegios.find())


@router.get("/{id_colegio}", response_model=Colegio)
async def player(id_colegio: str):
    return search_colegio_id(id_colegio)


@router.post("/", response_model=Colegio, status_code=201)
async def add_colegio(colegio: Colegio):
    if type(search_colegio(colegio.nombre)) == Colegio:
        raise HTTPException(status_code=409, detail="El colegio ya existe")
    
    colegio_dict = colegio.model_dump()
    del colegio_dict["id"]

    id = db_client.test.colegios.insert_one(colegio_dict).inserted_id

    colegio_dict["id"] = str(id)
    return Colegio(**colegio_dict)


@router.delete("/{id_colegio}", response_model=Colegio)
async def delete_colegio(id_colegio: str):
    
    found = db_client.test.colegios.find_one_and_delete({"_id":ObjectId(id_colegio)})

    if not found:
        raise HTTPException(status_code=404, detail="Colegio no encontrado")
    
    alumno_data = alumnos_schema(db_client.test.alumnos.find({"id_colegio": id_colegio}))
    
    for alumno in alumno_data:
        delete_alumno(alumno.id)
    
    return Colegio(**colegio_schema(found))


def search_colegio_id(id: str):    
    
    colegio_data = db_client.test.colegios.find_one({"_id": ObjectId(id)})

    if not colegio_data:
        raise HTTPException(status_code=404, detail="Colegio no encontrado")
    
    colegio = colegio_schema(colegio_data)

    return Colegio(**colegio)


def search_colegio(nombre: str):
    try:
        colegio = colegio_schema(db_client.test.colegio.find_one({"nombre": nombre}))
        return Colegio(**colegio)
    except:
        return {"error": "Colegio no encontrado"}


def delete_alumno(id_alumno:str):
    
    found = db_client.test.alumnos.find_and_delete({"id_colegio":ObjectId(id_alumno)})

    if not found:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return Alumno(**alumno_schema(found))
