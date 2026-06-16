from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.backend.database import get_db
from app.backend.schemas.crianca import CriancaSchema
from app.backend.models.crianca import CriancaModels

crianca = APIRouter()


# Criar criança

@crianca.post("/")
async def criar_crianca(
    dados: CriancaSchema,
    db: Session = Depends(get_db)
):
    nova_crianca = CriancaModels(**dados.model_dump())
    db.add(nova_crianca)
    db.commit()
    db.refresh(nova_crianca)
    return nova_crianca

@crianca.get("/")
async def listar_criancas(
    db: Session = Depends(get_db)
):
    return db.query(CriancaModels).all()


# Buscar criança por ID

@crianca.get("/{id}")
async def buscar_crianca(
    id: int,
    db: Session = Depends(get_db)
):
    crianca_encontrada = db.query(
        CriancaModels
    ).filter(
        CriancaModels.id == id
    ).first()
    if not crianca_encontrada:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Crianca com ID {id} nao encontrada"
        )
    return crianca_encontrada

# Atualizar criança

@crianca.put("/atualizar/{id}")
async def atualizar_crianca(
    id: int,
    dados: CriancaSchema,
    db: Session = Depends(get_db)
):
    crianca_atualizar = db.query(
        CriancaModels
    ).filter(
        CriancaModels.id == id
    ).first()
    if not crianca_atualizar:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Crianca com ID {id} nao encontrada"
        )
    for key, value in dados.model_dump().items():
        setattr(crianca_atualizar, key, value)
    db.commit()
    db.refresh(crianca_atualizar)
    return crianca_atualizar

#deletar criança

@crianca.delete("/deletar/{id}")
async def deletar_crianca(
    id: int,
    db: Session = Depends(get_db)
):
    crianca_deletar = db.query(
        CriancaModels
    ).filter(
        CriancaModels.id == id
    ).first()
    if not crianca_deletar:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Crianca com ID {id} nao encontrada"
        )
    db.delete(crianca_deletar)
    db.commit()
    return {
        "mensagem": "Crianca deletada com sucesso"
    }