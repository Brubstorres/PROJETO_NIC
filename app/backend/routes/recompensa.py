from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.backend.database.database import get_db
from app.backend.models.recompensa import RecompensaModels
from app.backend.schemas.recompensa import RecompensaSchema

recompensa = APIRouter()

# --------------------------------------------------------
# Criar recompensa

@recompensa.post("/")
async def criar_recompensa(
    dados: RecompensaSchema,
    db: Session = Depends(get_db)
):

    nova_recompensa = RecompensaModels(
        **dados.model_dump()
    )

    db.add(nova_recompensa)

    db.commit()

    db.refresh(nova_recompensa)

    return nova_recompensa


# --------------------------------------------------------
# Listar recompensas

@recompensa.get("/listar")
async def listar_recompensas(
    db: Session = Depends(get_db)
):

    return db.query(RecompensaModels).all()


# --------------------------------------------------------
# Buscar recompensa por ID

@recompensa.get("/{id}")
async def buscar_recompensa(
    id: int,
    db: Session = Depends(get_db)
):

    recompensa_encontrada = db.query(
        RecompensaModels
    ).filter(
        RecompensaModels.id == id
    ).first()

    if not recompensa_encontrada:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recompensa com ID {id} não encontrada"
        )

    return recompensa_encontrada


# --------------------------------------------------------
# Atualizar recompensa

@recompensa.put("/atualizar/{id}")
async def atualizar_recompensa(
    id: int,
    dados: RecompensaSchema,
    db: Session = Depends(get_db)
):

    recompensa_atualizar = db.query(
        RecompensaModels
    ).filter(
        RecompensaModels.id == id
    ).first()

    if not recompensa_atualizar:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recompensa com ID {id} não encontrada"
        )

    for key, value in dados.model_dump().items():

        setattr(
            recompensa_atualizar,
            key,
            value
        )

    db.commit()

    db.refresh(
        recompensa_atualizar
    )

    return recompensa_atualizar


# --------------------------------------------------------
# Deletar recompensa

@recompensa.delete("/deletar/{id}")
async def deletar_recompensa(
    id: int,
    db: Session = Depends(get_db)
):

    recompensa_deletar = db.query(
        RecompensaModels
    ).filter(
        RecompensaModels.id == id
    ).first()

    if not recompensa_deletar:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recompensa com ID {id} não encontrada"
        )

    db.delete(
        recompensa_deletar
    )

    db.commit()

    return {
        "mensagem": "Recompensa deletada com sucesso"
    }