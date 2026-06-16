from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.backend.database.database import get_db
from app.backend.models.usuario import UsuarioModels
from app.backend.schemas.usuario import UsuarioSchema

usuario = APIRouter()

# Criar usuário

@usuario.post("/")
async def criar_usuario(
    dados: UsuarioSchema,
    db: Session = Depends(get_db)
):

    novo_usuario = UsuarioModels(**dados.model_dump())

    db.add(novo_usuario)

    db.commit()

    db.refresh(novo_usuario)

    return novo_usuario

# Listar usuários

@usuario.get("/listar")
async def listar_usuarios(
    db: Session = Depends(get_db)
):

    return db.query(UsuarioModels).all()

# Buscar usuário por ID

@usuario.get("/{id}")
async def buscar_usuario(
    id: int,
    db: Session = Depends(get_db)
):

    usuario_encontrado = db.query(
        UsuarioModels
    ).filter(
        UsuarioModels.id == id
    ).first()

    if not usuario_encontrado:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuário com ID {id} não encontrado"
        )

    return usuario_encontrado

# Atualizar usuário

@usuario.put("/atualizar/{id}")
async def atualizar_usuario(
    id: int,
    dados: UsuarioSchema,
    db: Session = Depends(get_db)
):

    usuario_atualizar = db.query(
        UsuarioModels
    ).filter(
        UsuarioModels.id == id
    ).first()

    if not usuario_atualizar:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuário com ID {id} não encontrado"
        )

    for key, value in dados.model_dump().items():

        setattr(
            usuario_atualizar,
            key,
            value
        )

    db.commit()

    db.refresh(
        usuario_atualizar
    )

    return usuario_atualizar

# Deletar usuário

@usuario.delete("/deletar/{id}")
async def deletar_usuario(
    id: int,
    db: Session = Depends(get_db)
):

    usuario_deletar = db.query(
        UsuarioModels
    ).filter(
        UsuarioModels.id == id
    ).first()

    if not usuario_deletar:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuário com ID {id} não encontrado"
        )

    db.delete(
        usuario_deletar
    )

    db.commit()

    return {
        "mensagem": "Usuário deletado com sucesso"
    }