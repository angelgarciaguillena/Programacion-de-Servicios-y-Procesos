from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import player, team, team_db, player_db, auth_users

app = FastAPI()

app.include_router(team.router)
app.include_router(player.router)
app.include_router(auth_users.router)
app.include_router(team_db.router)
app.include_router(player_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"hello" : "world"}