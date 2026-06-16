from pydantic import BaseModel
from typing import Optional

class Questionario(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    nivel_suporte: Optional[str] = None
    fala: bool = False
    escreve: bool = False
    sabe_ler: bool = False
    reativo: bool = False
    preferencias: Optional[str] = None
    hipersensibilidade: Optional[str] = None
    hiposensibilidade: Optional[str] = None

    class Config:
        from_attributes = True
