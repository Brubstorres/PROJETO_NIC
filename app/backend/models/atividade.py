from app.backend.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey

class Atividade(Base):
    __tablename__ = "atividades"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(Text)
    tipo = Column(String)
    categoria = Column(String)
    dificuldade = Column(String)
    nivel = Column(Integer)
    imagem = Column(String)
    audio = Column(String)
    pontos = Column(Integer)

    recompensa_id = Column(Integer, ForeignKey("recompensas.id"))
    