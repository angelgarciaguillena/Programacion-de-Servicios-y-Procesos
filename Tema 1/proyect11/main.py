from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from player import player
from team import team

app = FastAPI()

app.include_router(team.router)
app.include_router(player.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"hello" : "world"}