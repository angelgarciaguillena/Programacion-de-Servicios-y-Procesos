from typing import Optional
from pydantic import BaseModel

class Client(BaseModel):
    id: Optional[str]
    dni: str
    name: str
    last_name: str
    phone: int
    mail: str