from datetime import datetime, timedelta, timezone
from db.models.user import User, UserDB
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


import jwt

from jwt.exceptions import PyJWTError

from pwdlib import PasswordHash

SECRET_KEY = "588d08f37f3c51a11a363d767d4ac9ebd4fc1b11b0c784e701d760ceb27e52d9"

ALGORITHM = "HS256"

ACCES_TOKEN_EXPIRE_MINUTES = 5

password_hash = PasswordHash.recommended()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter()

users_db = {
    "prueba" : {
        "username": "prueba",
        "fullname": "Prueba",
        "email": "prueba1@iesnervion.es",
        "disabled": False,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$SqQ7YQjX1+swmSa4WtVLTA$Lb+xzfYl5jl/OfrW+UMP90FQzIQdUqhWb1ArgNH8xd8"
    }
}

@router.post("/auth/registro", status_code = 201)
async def register(user: UserDB):
    if user.username not in users_db:
        hashed_password = password_hash.hash(user.password)
        user.password = hashed_password
        users_db[user.username] = user.model_dump()
        return user
    raise HTTPException(status_code = 409, detail = "El usuario ya existe")

@router.post("/auth/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    
    user_db = users_db.get(form.username)
    
    if user_db:
        user = UserDB(**user_db)

        try:
            if password_hash.verify(form.password, user.password):
                
                expire = datetime.now(timezone.utc) + timedelta(minutes = ACCES_TOKEN_EXPIRE_MINUTES)
                
                access_token = {"sub" : user.username, "exp" : expire}
                
                token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
                
                return {"access_token": token, "token_type": "bearer"}
        except:
            raise HTTPException(status_code = 400, detail = "Error en la autenticacion")
    raise HTTPException(status_code = 401, detail = "Usuario o contraseña incorrectos")


async def get_current_user(token: str = Depends(oauth2)):
    
    try:
        username = jwt.decode(token, SECRET_KEY, algorithm = ALGORITHM).get("sub")
        
        if username is None:
            raise HTTPException(status_code = 401, detail = "Credenciales de autenticacion invalidas",
                                headers={"WW-Authenticate" : "Bearer"})
    except PyJWTError:
        raise HTTPException(status_code = 401, detail = "Credenciales de autenticacion invalidas",
                                headers={"WW-Authenticate" : "Bearer"})
    
    user = User(**users_db[username])
    
    if user.disabled:
        raise HTTPException(status_code = 400, detail = "Usuario inactivo")
    
    return user


@router.get("/auth/me")
async def me(user: User = Depends(get_current_user)):
    return user