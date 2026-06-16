from pydantic import BaseModel
from typing import Optional

class Atividade(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: str
    tipo: str
    categoria: str
    dificuldade: str
    nivel: int
    imagem: str
    audio: str
    pontos: int
    recompensa_id: int

    class Config:
        from_attributes = True
