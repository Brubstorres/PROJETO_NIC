from app.backend.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey

class Recompensa(Base):
    __tablename__ = "recompensas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    pontos = Column(Integer)

    atividades_id = Column(Integer, ForeignKey("atividades.id"))
    crianca_id = Column(Integer, ForeignKey("criancas.id"))