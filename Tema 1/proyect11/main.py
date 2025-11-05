from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.player import player
from routers.team import team
from routers import auth_users

app = FastAPI()

app.include_router(team.router)
app.include_router(player.router)
app.include_router(auth_users.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"hello" : "world"}