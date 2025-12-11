from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix = "/clients", tags = ["clients"])

#region Clase Cliente
class Client(BaseModel):
    id: int
    dni: str
    name: str
    last_name: str
    phone: int
    mail: str
#endregion

#region Listado Clientes
client_list = [
    Client(id=1, dni="12345678A", name="Juan", last_name="Pérez", phone=600123456, mail="juan.perez@example.com"),
    Client(id=2, dni="87654321B", name="María", last_name="Gómez", phone=600654321, mail="maria.gomez@example.com"),
    Client(id=3, dni="11223344C", name="Luis", last_name="Martínez", phone=600112233, mail="luis.martinez@example.com"),
    Client(id=4, dni="44332211D", name="Ana", last_name="López", phone=600443322, mail="ana.lopez@example.com"),
    Client(id=5, dni="55667788E", name="Carlos", last_name="Sánchez", phone=600556677, mail="carlos.sanchez@example.com"),
]
#endregion

#region Funciones
def next_id():
    return (max(client_list, key = id).id + 1)


def search_client(id: int):
    return [client for client in client_list if client.id == id]
#endregion


#region Metodos get
@router.get("/")
def get_clients():
    return client_list

@router.get("/{id_client}")
def get_by_id_client(id_client: int):

    clients = search_client(id_client)

    if len(clients) != 0:
        return clients[0]
    
    else:
        raise HTTPException(status_code = 404, detail = "Client not found")
#endregion

#region Metodo post
@router.post("/", status_code = 201)
def add_client(client: Client):

    client.id = next_id()

    client_list.append(client)

    return client
#endregion

#region Metodo put
@router.put("/{id_client}", response_model = Client)
def modify_client(id_client: int, client: Client):

    for index, saved_client in enumerate(client_list):

        if saved_client.id == id_client:

            client.id = id_client

            client_list[index] = client

            return client
        
    raise HTTPException(status_code = 404, detail = "Client not found")
#endregion

#region Metodo delete
@router.delete("/{id_client}")
def delete_client(id_client: int):

    for saved_client in client_list:

        if saved_client.id == id_client:

            client_list.remove(saved_client)

            return {}
        
    raise HTTPException(status_code = 404, detail = "Client not found")
#endregion