# Proyecto: Sistema de Notas

Aplicación fullstack de gestión de notas con **FastAPI** (backend), **HTML/JS vanilla** (frontend) y **PostgreSQL** (base de datos).

---

## Requisitos previos

- Python 3.12+
- PostgreSQL instalado y corriendo
- Un navegador web moderno

---

## 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd proyecto_notas
```

---

## 2. Instalar dependencias del backend

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
source venv/bin/activate          # Linux / macOS
# o
venv\Scripts\activate             # Windows

# Instalar dependencias
pip install fastapi psycopg2-binary uvicorn
```

---

## 3. Levantar la base de datos (PostgreSQL)

Asegúrate de que PostgreSQL esté corriendo:

```bash
sudo systemctl start postgresql    # Linux
# o inicia PostgreSQL desde tu panel de control en Windows / macOS
```

Ejecuta el script SQL para crear la BD, las tablas y los datos de ejemplo:

```bash
psql -U postgres -f database.sql
```

> Si te pide contraseña, usa la de tu usuario `postgres`. Los valores de conexión del backend están configurados como:
> - **Host:** `localhost`
> - **BD:** `notas_db`
> - **Usuario:** `postgres`
> - **Contraseña:** `1234`
>
> Modifica `main.py` → función `get_db()` si tus credenciales son distintas.

---

## 4. Arrancar el backend

```bash
# (con el entorno virtual activado)
fastapi dev main.py
```

El backend estará disponible en: **http://127.0.0.1:8000**

Documentación interactiva (Swagger): **http://127.0.0.1:8000/docs**

---

## 5. Arrancar el frontend

El frontend son archivos HTML estáticos. Solo ábrelos en tu navegador:

**Opción A — Abrir directamente:**
```bash
# Doble clic o desde terminal:
xdg-open frontend/index.html        # Linux
open frontend/index.html            # macOS
start frontend/index.html           # Windows
```

**Opción B — Servir con Python (recomendado):**
```bash
cd frontend
python -m http.server 5500
```

Luego abre: **http://localhost:5500**

---

## Estructura del proyecto

```
proyecto_notas/
├── main.py            # Backend FastAPI (CRUD de notas)
├── database.sql       # Script SQL para crear BD y tablas
├── frontend/
│   ├── index.html     # Página para crear notas
│   └── ver.html       # Página para ver listado de notas
├── venv/              # Entorno virtual Python
└── READMI.md          # Este archivo
```

---

## Endpoints de la API

| Método | Ruta         | Descripción            |
|--------|-------------|------------------------|
| GET    | `/`          | Health check           |
| GET    | `/notas`     | Obtener todas las notas|
| POST   | `/notas`     | Crear una nueva nota   |
| PUT    | `/notas/{id}`| Actualizar una nota    |
| DELETE | `/notas/{id}`| Eliminar una nota      |

---

## Resumen rápido (todo en orden)

```bash
# 1. Clonar
git clone <URL> && cd proyecto_notas

# 2. Instalar
python -m venv venv && source venv/bin/activate
pip install fastapi psycopg2-binary uvicorn

# 3. BD
sudo systemctl start postgresql
psql -U postgres -f database.sql

# 4. Backend
fastapi dev main.py

# 5. Frontend (otra terminal)
cd frontend && python -m http.server 5500
```
