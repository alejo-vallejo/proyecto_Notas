from fastapi import APIRouter, HTTPException
from backend.schemas import UsuarioCreate, UsuarioLogin
from backend.services.usuarios_service import (
    create_usuario,
    authenticate,
    get_all_usuarios,
    get_usuario_by_id,
)

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.get("")
def listar_usuarios():
    return get_all_usuarios()


@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int):
    user = get_usuario_by_id(usuario_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@router.post("/registro")
def registrar_usuario(usuario: UsuarioCreate):
    try:
        nuevo = create_usuario(usuario.nombre, usuario.password)
        return nuevo
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login(usuario: UsuarioLogin):
    user = authenticate(usuario.nombre, usuario.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return user
