from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.backend.database.database import get_db
from app.backend.models.progresso import ProgressoModels
from app.backend.schemas.progresso import ProgressoSchema

progresso = APIRouter()

# --------------------------------------------------------
# Criar progresso

@progresso.post("/")
async def criar_progresso(
    dados: ProgressoSchema,
    db: Session = Depends(get_db)
):

    novo_progresso = ProgressoModels(
        **dados.model_dump()
    )

    db.add(novo_progresso)

    db.commit()

    db.refresh(novo_progresso)

    return novo_progresso


# --------------------------------------------------------
# Listar progresso

@progresso.get("/listar")
async def listar_progresso(
    db: Session = Depends(get_db)
):

    return db.query(ProgressoModels).all()


# --------------------------------------------------------
# Buscar progresso por ID

@progresso.get("/{id}")
async def buscar_progresso(
    id: int,
    db: Session = Depends(get_db)
):

    progresso_encontrado = db.query(
        ProgressoModels
    ).filter(
        ProgressoModels.id == id
    ).first()

    if not progresso_encontrado:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Progresso com ID {id} não encontrado"
        )

    return progresso_encontrado


# --------------------------------------------------------
# Atualizar progresso

@progresso.put("/atualizar/{id}")
async def atualizar_progresso(
    id: int,
    dados: ProgressoSchema,
    db: Session = Depends(get_db)
):

    progresso_atualizar = db.query(
        ProgressoModels
    ).filter(
        ProgressoModels.id == id
    ).first()

    if not progresso_atualizar:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Progresso com ID {id} não encontrado"
        )

    for key, value in dados.model_dump().items():

        setattr(
            progresso_atualizar,
            key,
            value
        )

    db.commit()

    db.refresh(
        progresso_atualizar
    )

    return progresso_atualizar


# --------------------------------------------------------
# Deletar progresso

@progresso.delete("/deletar/{id}")
async def deletar_progresso(
    id: int,
    db: Session = Depends(get_db)
):

    progresso_deletar = db.query(
        ProgressoModels
    ).filter(
        ProgressoModels.id == id
    ).first()

    if not progresso_deletar:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Progresso com ID {id} não encontrado"
        )

    db.delete(
        progresso_deletar
    )

    db.commit()

    return {
        "mensagem": "Progresso deletado com sucesso"
    }