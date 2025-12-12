from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import alumnos, colegios, auth_users

app = FastAPI()

# Routers
app.include_router(alumnos.router)
app.include_router(colegios.router)
app.include_router(auth_users.router)

@app.get("/")
def root():
    return {"hello" : "world"}