from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.backend.database.database import get_db
from app.backend.models.questionario import QuestionarioModels
from app.backend.schemas.questionario import QuestionarioSchema

questionario = APIRouter()

# --------------------------------------------------------
# Criar questionário

@questionario.post("/")
async def criar_questionario(
    dados: QuestionarioSchema,
    db: Session = Depends(get_db)
):

    novo_questionario = QuestionarioModels(
        **dados.model_dump()
    )

    db.add(novo_questionario)

    db.commit()

    db.refresh(novo_questionario)

    return novo_questionario


# --------------------------------------------------------
# Listar questionários

@questionario.get("/listar")
async def listar_questionarios(
    db: Session = Depends(get_db)
):

    return db.query(QuestionarioModels).all()


# --------------------------------------------------------
# Buscar questionário por ID

@questionario.get("/{id}")
async def buscar_questionario(
    id: int,
    db: Session = Depends(get_db)
):

    questionario_encontrado = db.query(
        QuestionarioModels
    ).filter(
        QuestionarioModels.id == id
    ).first()

    if not questionario_encontrado:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Questionário com ID {id} não encontrado"
        )

    return questionario_encontrado


# --------------------------------------------------------
# Atualizar questionário

@questionario.put("/atualizar/{id}")
async def atualizar_questionario(
    id: int,
    dados: QuestionarioSchema,
    db: Session = Depends(get_db)
):

    questionario_atualizar = db.query(
        QuestionarioModels
    ).filter(
        QuestionarioModels.id == id
    ).first()

    if not questionario_atualizar:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Questionário com ID {id} não encontrado"
        )

    for key, value in dados.model_dump().items():

        setattr(
            questionario_atualizar,
            key,
            value
        )

    db.commit()

    db.refresh(
        questionario_atualizar
    )

    return questionario_atualizar


# --------------------------------------------------------
# Deletar questionário

@questionario.delete("/deletar/{id}")
async def deletar_questionario(
    id: int,
    db: Session = Depends(get_db)
):

    questionario_deletar = db.query(
        QuestionarioModels
    ).filter(
        QuestionarioModels.id == id
    ).first()

    if not questionario_deletar:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Questionário com ID {id} não encontrado"
        )

    db.delete(
        questionario_deletar
    )

    db.commit()

    return {
        "mensagem": "Questionário deletado com sucesso"
    }