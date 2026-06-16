from pydantic import BaseModel
from typing import Optional

class ProgressoSchema(BaseModel):
    id: Optional[int] = None
    crianca_id: int
    atividadesRealizadas: int = 0
    totalPontos: int = 0
    recompensasResgatadas: int = 0

    class Config:
        from_attributes = True
