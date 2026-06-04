from fastapi import APIRouter, HTTPException, Query
from backend.schemas import NotaCreate, NotaUpdate
from backend.services.notas_service import (
    get_all_notas,
    get_nota_by_id,
    create_nota,
    update_nota,
    delete_nota,
)

router = APIRouter(prefix="/notas", tags=["Notas"])


@router.get("")
def listar_notas(usuario_id: int = Query(None)):
    notas = get_all_notas(usuario_id)
    return notas


@router.get("/{nota_id}")
def obtener_nota(nota_id: int):
    nota = get_nota_by_id(nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return nota


@router.post("")
def crear_nota(nota: NotaCreate):
    if not nota.titulo or not nota.contenido:
        raise HTTPException(status_code=400, detail="Faltan datos")
    nueva = create_nota(nota.titulo, nota.contenido, nota.usuario_id)
    return nueva


@router.put("/{nota_id}")
def actualizar_nota(nota_id: int, nota: NotaUpdate):
    actualizada = update_nota(nota_id, nota.titulo, nota.contenido)
    if not actualizada:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return actualizada


@router.delete("/{nota_id}")
def eliminar_nota(nota_id: int):
    eliminado = delete_nota(nota_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return {"mensaje": "Nota eliminada correctamente"}
