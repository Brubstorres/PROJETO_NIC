from app.backend.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean

class educacional(Base):
    __tablename__ = "educacional"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    escola = Column(String)
    serie = Column(Integer)
    email = Column(String, unique = True, index = True)
    senha = Column(String) 
    nomeEscola = Column(String)

    crianca_id = Column(Integer, ForeignKey("criancas.id"))
   
    