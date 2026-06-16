from pydantic import BaseModel
from typing import Optional

class EducacionalSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    escola: Optional[str] = None
    serie: Optional[int] = None
    email: str
    senha: str
    nomeEscola: Optional[str] = None
    crianca_id: int

    class Config:
        from_attributes = True
