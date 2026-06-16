from app.backend.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey

class Progresso(Base):
    __tablename__ = "progresso"

    id = Column(Integer, primary_key=True, index=True)
    crianca_id = Column(Integer, ForeignKey("criancas.id"))
    atividadesRealizadas = Column(Integer)
    totalPontos = Column(Integer)
    recompensasResgatadas = Column(Integer)
    
