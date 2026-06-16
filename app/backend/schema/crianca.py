from pydantic import BaseModel
from typing import Optional
from datetime import date

class Crianca(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    genero: Optional[str] = None
    data_nascimento: Optional[date] = None
    responsavel_id: int

    class Config:
        from_attributes = True
