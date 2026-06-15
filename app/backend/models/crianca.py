from sqlalchemy import string, Integer, Column
from app.database import Base

class Crianca(Base):
    __tablename__ = "criancas"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    genero = Column(String)
    data_nascimento = Column(Date)
    
    responsavel_id = Column(Integer, ForeignKey("responsavels.id"))
    