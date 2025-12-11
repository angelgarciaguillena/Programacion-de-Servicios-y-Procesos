from fastapi import FastAPI
from routers import client, product, auth_users, product_db, client_db

app = FastAPI()

app.include_router(client.router)
app.include_router(product.router)
app.include_router(auth_users.router)
app.include_router(product_db.router)
app.include_router(client_db.router)


@app.get("/")
def root():
    return {"hello": "world"}