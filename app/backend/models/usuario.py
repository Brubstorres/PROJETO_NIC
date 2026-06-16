from app.backend.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean

class UsuarioModels(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    idade = Column(Integer)
    cidade = Column(String)
    estado = Column(String)
    pais = Column(String)
    cep = Column(String)
    telefone = Column(String)
    cpf = Column(String, unique = True, index = True)
    

    
    