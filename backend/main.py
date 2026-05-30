from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.notas import router as notas_router
from backend.routes.usuarios import router as usuarios_router
from backend.routes.ia import router as ia_router

app = FastAPI(
    title="Sistema de Notas",
    description="API para gestión de notas con PostgreSQL e IA",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notas_router)
app.include_router(usuarios_router)
app.include_router(ia_router)


@app.get("/")
def inicio():
    return {"mensaje": "API de notas funcionando correctamente"}
