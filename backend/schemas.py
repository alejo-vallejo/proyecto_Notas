from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NotaBase(BaseModel):
    titulo: str
    contenido: str


class NotaCreate(NotaBase):
    usuario_id: Optional[int] = 1


class NotaUpdate(BaseModel):
    titulo: Optional[str] = None
    contenido: Optional[str] = None


class NotaOut(NotaBase):
    id: int
    fecha: Optional[datetime] = None
    usuario_id: Optional[int] = None


class UsuarioCreate(BaseModel):
    nombre: str
    password: str


class UsuarioOut(BaseModel):
    id: int
    nombre: str


class UsuarioLogin(BaseModel):
    nombre: str
    password: str


class IATextoRequest(BaseModel):
    texto: str


class IATextoResponse(BaseModel):
    texto_mejorado: str
