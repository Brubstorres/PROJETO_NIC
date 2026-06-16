from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.backend.database import get_db
from app.backend.schemas.atividade import AtividadeSchema
from app.backend.models.atividade import AtividadeModels

atividade = APIRouter()


# Criar atividade

@atividade.post("/")
async def criar_atividade(
    dados: AtividadeSchema,
    db: Session = Depends(get_db)
):
    nova_atividade = AtividadeModels(**dados.model_dump())
    db.add(nova_atividade)
    db.commit()
    db.refresh(nova_atividade)
    return nova_atividade

@atividade.get("/")
async def listar_atividades(
    db: Session = Depends(get_db)
):
    return db.query(AtividadeModels).all()


# Buscar atividade por ID

@atividade.get("/{id}")
async def buscar_atividade(
    id: int,
    db: Session = Depends(get_db)
):
    atividade_encontrada = db.query(
        AtividadeModels
    ).filter(
        AtividadeModels.id == id
    ).first()
    if not atividade_encontrada:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atividade com ID {id} nao encontrada"
        )
    return atividade_encontrada

# Atualizar atividade

@atividade.put("/atualizar/{id}")
async def atualizar_atividade(
    id: int,
    dados: AtividadeSchema,
    db: Session = Depends(get_db)
):
    atividade_atualizar = db.query(
        AtividadeModels
    ).filter(
        AtividadeModels.id == id
    ).first()
    if not atividade_atualizar:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atividade com ID {id} nao encontrada"
        )
    for key, value in dados.model_dump().items():
        setattr(atividade_atualizar, key, value)
    db.commit()
    db.refresh(atividade_atualizar)
    return atividade_atualizar

#deletar atividade

@atividade.delete("/deletar/{id}")
async def deletar_atividade(
    id: int,
    db: Session = Depends(get_db)
):
    atividade_deletar = db.query(
        AtividadeModels
    ).filter(
        AtividadeModels.id == id
    ).first()
    if not atividade_deletar:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atividade com ID {id} nao encontrada"
        )
    db.delete(atividade_deletar)
    db.commit()
    return {
        "mensagem": "Atividade deletada com sucesso"
    }