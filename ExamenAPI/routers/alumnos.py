from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.schemas.alumno import alumno_schema, alumnos_schema
from db.models.alumno import Alumno
from db.client import db_client

from bson import ObjectId

router = APIRouter(prefix="/alumnos", tags=["alumnos"])

alumnos_list = []

@router.get("/", response_model = list[Alumno])
async def alumnos():
    return alumnos_schema(db_client.test.alumnos.find())


@router.get("/{curso}}", response_model= list[Alumno])
async def alumnos_curso(curso: str):
    return alumnos_schema(db_client.test.alumnos.find({"curso": curso}))


@router.get("/{distrito}}", response_model= list[Alumno])
async def alumnos_distrito(distrito: str):
    return alumnos_schema(db_client.test.alumnos.find({"distrito": distrito}))


@router.get("/colegios/{id_colegio}/alumnos", response_model= list[Alumno])
async def alumnos_colegio(id_colegio: str):
    return alumnos_schema(db_client.test.alumnos.find({"id_colegio": id_colegio}))


@router.post("/", response_model=Alumno, status_code=201)
async def add_alumno(alumno: Alumno):
    if type(search_alumno(alumno.nombre)) == Alumno:
        raise HTTPException(status_code=409, detail="El alumno ya existe")
    
    alumno_dict = alumno.model_dump()
    del alumno_dict["id"]

    id = db_client.test.alumnos.insert_one(alumno_dict).inserted_id

    alumno_dict["id"] = str(id)
    return Alumno(**alumno_dict)


@router.put("/{id_alumno}", response_model=Alumno)
async def modify_alumno(id_alumno: str, new_alumno: Alumno):
    
    alumno_dict = new_alumno.model_dump()

    del alumno_dict["id"]   
    updated = db_client.test.alumnos.find_one_and_replace({"_id": ObjectId(id_alumno)}, alumno_dict)

    if not updated:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return search_alumno_id(id_alumno)


@router.delete("/{id_alumno}", response_model=Alumno)
async def delete_alumno(id_alumno:str):
    
    found = db_client.test.alumnos.find_one_and_delete({"_id":ObjectId(id_alumno)})

    if not found:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return Alumno(**alumno_schema(found))



def search_alumno_id(id: str):    
    
    alumno_data = db_client.test.alumnos.find_one({"_id": ObjectId(id)})

    if not alumno_data:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    
    alumno = alumno_schema(alumno_data)

    return Alumno(**alumno)
    
        
def search_alumno(nombre: str):
    try:
        alumno = alumno_schema(db_client.test.alumnos.find_one({"nombre": nombre}))
        return Alumno(**alumno)
    except:
        return {"error": "Alumno no encontrado"}