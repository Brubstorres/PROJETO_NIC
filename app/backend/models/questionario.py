from app.backend.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean

class Questionario(Base):
    __tablename__ = "questionarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idade = Column(Integer)
    nivel_suporte = Column(String, nullable=True)
    fala = Column(Boolean, default=False)
    escreve = Column(Boolean, default=False)
    sabe_ler = Column(Boolean, default=False)
    reativo = Column(Boolean, default=False)
    preferencias = Column(Text, nullable=True)
    hipersensibilidade = Column(Text, nullable=True)
    hiposensibilidade = Column(Text, nullable=True)