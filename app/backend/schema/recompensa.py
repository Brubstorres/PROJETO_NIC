from pydantic import BaseModel
from typing import Optional

class Recompensa(BaseModel):
    id: Optional[int] = None
    nome: str
    pontos: int
    atividades_id: Optional[int] = None
    crianca_id: Optional[int] = None

    class Config:
        from_attributes = True
