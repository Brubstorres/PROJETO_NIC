from fastapi import FastAPI
from app.backend.database import engine, Base

##---------------------------MODULOS DAS ROTAS--------------------------------##

from app.backend.routes.atividade import atividade
from app.backend.routes.crianca import crianca
from app.backend.routes.educacional import educacional
from app.backend.routes.questionario import questionario
from app.backend.routes.progresso import progresso
from app.backend.routes.recompensa import recompensa
from app.backend.routes.usuario import usuario

##----------------------------------------------------------------------------##

#Base.metadata.drop_all(bind=engine)
#deleta todos os dados do banco de dados

Base.metadata.create_all(bind=engine)
#cria os dados do banco de dados

#injecao de dependecia
app = FastAPI()
app.include_router(atividade, prefix="/atividade", tags=["atividade"])
app.include_router(crianca, prefix="/crianca", tags=["crianca"])
app.include_router(educacional, prefix="/educacional", tags=["educacional"])
app.include_router(questionario, prefix="/questionario", tags=["questionario"])
app.include_router(progresso, prefix="/progresso", tags=["progresso"])
app.include_router(recompensa, prefix="/recompensa", tags=["recompensa"])
app.include_router(usuario, prefix="/usuario", tags=["usuario"])


@app.get("/")
def read_root():
    return {"fofinho": "palandi"}