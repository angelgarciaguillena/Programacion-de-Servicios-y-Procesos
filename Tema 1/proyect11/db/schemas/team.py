def team_schema(team) -> dict:
    # El id en base de datos es _id
    return {"id": str(team["_id"]),
            "name": team["name"],
            "city": team["city"],
            "year_founded": team["year_founded"],
            "stadium": team["stadium"],}
    
def teams_schema(teams) -> list:
    return [team_schema(team) for team in teams]