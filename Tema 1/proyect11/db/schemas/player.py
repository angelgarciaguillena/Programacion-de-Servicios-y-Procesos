def player_schema(player) -> dict:
    # El id en base de datos es _id
    return {"id": str(player["_id"]),
            "name": player["name"],
            "age": player["age"],
            "position": player["position"],
            "nationality": player["nationality"],
            "salary": player["salary"],
            "id_team": player["id_team"]}
    
def players_schema(players) -> list:
    return [player_schema(player) for player in players]