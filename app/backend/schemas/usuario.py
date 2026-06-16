from pydantic import BaseModel
from typing import Optional

class UsuarioSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    senha: str
    idade: Optional[int] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    pais: Optional[str] = None
    cep: Optional[str] = None
    telefone: Optional[str] = None
    cpf: Optional[str] = None

    class Config:
        from_attributes = True
