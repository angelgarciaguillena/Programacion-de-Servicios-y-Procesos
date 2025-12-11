from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: Optional[str]
    name: str
    description: str
    price: float
    idClient: Optional[str]
