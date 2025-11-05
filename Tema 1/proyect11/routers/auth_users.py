from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

#Clave de cifrado para el token
SECRET_KEY = "588d08f37f3c51a11a363d767d4ac9ebd4fc1b11b0c784e701d760ceb27e52d9"

#Algoritmo para cifrar el token
ALGORITHM = "HS256"

#Duracion del token
ACCES_TOKEN_EXPIRE_MINUTES = 5

#Objeto que utilizaremos para el hash de la contraseña
password_hash = PasswordHash.recommended()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter()

class User(BaseModel):
    username: str 
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "angelgg" : {
        "username" : "angelgg",
        "fullname" : "Angel Garcia",
        "email" : "angel.garcia@iesnervion.es",
        "disabled" : False,
        "password" : "123456",
    },
    "prueba" : {
        "username": "prueba1",
        "fullname": "Prueba 1",
        "email": "prueba1@iesnervion.es",
        "disabled": False,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$SqQ7YQjX1+swmSa4WtVLTA$Lb+xzfYl5jl/OfrW+UMP90FQzIQdUqhWb1ArgNH8xd8"
    }
}

@router.post("/register", status_code = 201)
def register(user: UserDB):
    if user.username not in users_db:
        hashed_password = password_hash.hash(user.password)
        user.password = hashed_password
        users_db[user.username] = user
        return user
    raise HTTPException(status_code = 409, detail = "User already exists")