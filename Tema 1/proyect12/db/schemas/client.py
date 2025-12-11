def client_schema(client) -> dict:
    return {
        "id": str(client["_id"]),
        "dni": client["dni"],
        "name": client["name"],
        "last_name": client["last_name"],
        "phone": client["phone"],
        "mail": client["mail"]
    }

def clients_schema(clients) -> list:
    return [client_schema(client) for client in clients]