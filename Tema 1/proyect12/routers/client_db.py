from fastapi import APIRouter, HTTPException
from db.client import db_client
from db.models.client import Client
from db.schemas.client import client_schema, clients_schema
from bson import ObjectId

router = APIRouter(prefix = "/clientsdb", tags = ["clientsdb"])

clients_list = []


@router.get("/", response_model = list[Client])
async def clients():
    return clients_schema(db_client.test.clients.find())


@router.get("/{id_client}", response_model = Client)
async def client(id_client: str):
    return search_client_id(id_client)


@router.post("/", response_model = Client, status_code = 201)
async def add_client(client: Client):

    if type(search_client(client.dni)) == Client:
        raise HTTPException(status_code = 409, detail = "Client already exists")
    
    client_dict = client.model_dump()
    del client_dict["id"]

    id = db_client.test.clients.insert_one(client_dict).inserted_id

    client_dict["id"] = str(id)
    return Client(**client_dict)


@router.put("/{id_client}", response_model = Client)
async def modify_client(id_client: str, new_client: Client):

    client_dict = new_client.model_dump()

    del client_dict["id"]
    updated = db_client.test.clients.find_one_and_replace({"_id": ObjectId(id_client)}, client_dict)

    if not updated: 
        raise HTTPException(status_code = 404, detail = "Client not found")
    return search_client_id(id_client)


@router.delete("/{id_client}", response_model = Client)
async def delete_client(id_client: str):

    found = db_client.test.clients.find_one_and_delete({"_id": ObjectId(id_client)})

    if not found:
        raise HTTPException(status_code = 404, detail = "Client not found")
    return Client(**client_schema(found))


def search_client_id(id: str):

    client_data = db_client.test.clients.find_one({"_id": ObjectId(id)})

    if not client_data:
        raise HTTPException(status_code=404, detail="Client not found")
    
    client = client_schema(client_data)

    return Client(**client)


def search_client(dni: str):
    try:
        client = client_schema(db_client.test.clients.find_one({"dni": dni}))
        return Client(**client)
    except:
        return {"error": "Client not found"}

"""
def next_id():
    return (max(client.id for client in clients_list)) + 1"""