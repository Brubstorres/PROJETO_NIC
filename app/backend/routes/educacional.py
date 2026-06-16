from app.backend.schemas.educacional import EducacionalSchema
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.backend.database import get_db
from app.backend.schemas.educacional import EducacionalSchema
from app.backend.models.educacional import EducacionalModels

educacional = APIRouter()


# Criar educacional

@educacional.post("/")
async def criar_educacional(
    dados: EducacionalSchema,
    db: Session = Depends(get_db)
):
    nova_educacional = EducacionalModels(**dados.model_dump())
    db.add(nova_educacional)
    db.commit()
    db.refresh(nova_educacional)
    return nova_educacional

@educacional.get("/")
async def listar_educacionais(
    db: Session = Depends(get_db)
):
    return db.query(EducacionalModels).all()


# Buscar educacional por ID

@educacional.get("/{id}")
async def buscar_educacional(
    id: int,
    db: Session = Depends(get_db)
):
    educacional_encontrada = db.query(
        EducacionalModels
    ).filter(
        EducacionalModels.id == id
    ).first()
    if not educacional_encontrada:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Educacional com ID {id} nao encontrada"
        )
    return educacional_encontrada

# Atualizar educacional

@educacional.put("/atualizar/{id}")
async def atualizar_educacional(
    id: int,
    dados: EducacionalSchema,
    db: Session = Depends(get_db)
):
    educacional_atualizar = db.query(
        EducacionalModels
    ).filter(
        EducacionalModels.id == id
    ).first()
    if not educacional_atualizar:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Educacional com ID {id} nao encontrada"
        )
    for key, value in dados.model_dump().items():
        setattr(educacional_atualizar, key, value)
    db.commit()
    db.refresh(educacional_atualizar)
    return educacional_atualizar

#deletar educacional

@educacional.delete("/deletar/{id}")
async def deletar_educacional(
    id: int,
    db: Session = Depends(get_db)
):
    educacional_deletar = db.query(
        EducacionalModels
    ).filter(
        EducacionalModels.id == id
    ).first()
    if not educacional_deletar:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Educacional com ID {id} nao encontrada"
        )
    db.delete(educacional_deletar)
    db.commit()
    return {
        "mensagem": "Educacional deletada com sucesso"
    }