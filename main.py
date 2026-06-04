from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
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

app.mount("/css", StaticFiles(directory="frontend/css"), name="css")
app.mount("/js", StaticFiles(directory="frontend/js"), name="js")


@app.get("/")
def index():
    return FileResponse("frontend/index.html")


@app.get("/login")
def login_page():
    return FileResponse("frontend/login.html")


@app.get("/ver")
def ver_notas():
    return FileResponse("frontend/ver.html")


@app.get("/editar")
def editar_nota():
    return FileResponse("frontend/editar.html")


app.include_router(notas_router)
app.include_router(usuarios_router)
app.include_router(ia_router)
