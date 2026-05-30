# Sistema de Notas

API REST para gestión de notas personales con FastAPI, PostgreSQL e integración de Inteligencia Artificial.

## Tecnologías

- **Backend:** Python + FastAPI
- **Base de datos:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript vanilla
- **IA:** API compatible con OpenAI (Ollama, OpenAI, Hugging Face)

## Estructura del Proyecto

```
proyecto_notas/
├── backend/
│   ├── main.py              # Punto de entrada de FastAPI
│   ├── config.py             # Configuración (DB, IA)
│   ├── database.py           # Conexión y helpers de PostgreSQL
│   ├── schemas.py            # Modelos Pydantic de validación
│   ├── routes/
│   │   ├── notas.py          # CRUD de notas
│   │   ├── usuarios.py       # Gestión de usuarios
│   │   └── ia.py             # Endpoint de mejora con IA
│   ├── services/
│   │   ├── notas_service.py  # Lógica de negocio de notas
│   │   ├── usuarios_service.py  # Lógica de negocio de usuarios
│   │   └── ia_service.py     # Integración con IA
│   └── utils/
├── frontend/
│   ├── index.html            # Crear nota + Mejorar con IA
│   ├── ver.html              # Listar, editar y eliminar notas
│   ├── editar.html           # Editar nota + Mejorar con IA
│   ├── css/
│   │   └── style.css         # Estilos globales
│   └── js/
│       └── app.js            # Cliente API y utilidades
├── database/
│   └── database.sql          # Esquema y datos de prueba
├── requirements.txt
└── README.md
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/alejo-vallejo/proyecto_Notas.git
cd proyecto_Notas
```

### 2. Crear y activar entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Base de Datos

### 1. Iniciar PostgreSQL

```bash
sudo service postgresql start
```

### 2. Entrar a PostgreSQL

```bash
sudo -u postgres psql
```

### 3. Crear base de datos y ejecutar script

```sql
CREATE DATABASE notas_db;
\c notas_db;
\i database/database.sql;
```

Esto crea las tablas `usuarios` y `notas` e inserta datos de prueba.

## Ejecutar el Backend

Con el entorno virtual activado:

```bash
fastapi dev backend/main.py
```

El servidor se ejecutará en: **http://127.0.0.1:8000**

Documentación interactiva: **http://127.0.0.1:8000/docs**

## Ejecutar el Frontend

Abre los archivos HTML directamente en el navegador:

```bash
# Desde Linux con WSL
explorer.exe frontend/index.html
explorer.exe frontend/ver.html

# O simplemente abre los archivos con tu navegador
```

## Endpoints de la API

### Notas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/notas` | Listar todas las notas |
| GET | `/notas/{id}` | Obtener una nota por ID |
| POST | `/notas` | Crear una nota |
| PUT | `/notas/{id}` | Actualizar una nota |
| DELETE | `/notas/{id}` | Eliminar una nota |

### Usuarios

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/usuarios` | Listar usuarios |
| GET | `/usuarios/{id}` | Obtener un usuario |
| POST | `/usuarios/registro` | Registrar un usuario |
| POST | `/usuarios/login` | Iniciar sesión |

### Inteligencia Artificial

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/ia` | Mejorar texto con IA |

## Funcionalidad de IA

El botón **"Mejorar con IA"** en los formularios de crear y editar nota envía el texto al backend, que lo procesa a través de un modelo de lenguaje y devuelve una versión mejorada (corrección ortográfica, gramatical y de redacción).

### Configurar la IA

El sistema usa una API compatible con OpenAI. Por defecto intenta conectarse a **Ollama** (local y gratuito).

#### Opción 1: Ollama (recomendado, gratuito)

1. Instala Ollama desde [ollama.ai](https://ollama.ai)
2. Descarga un modelo: `ollama pull llama3`
3. Asegúrate que Ollama esté corriendo: `ollama serve`

#### Opción 2: OpenAI

```bash
export IA_API_URL="https://api.openai.com/v1/chat/completions"
export IA_API_KEY="tu-api-key"
export IA_MODEL="gpt-4o-mini"
```

#### Variables de entorno

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| `IA_API_URL` | URL de la API de IA | `http://localhost:11434/v1/chat/completions` |
| `IA_API_KEY` | API Key (si requiere) | `""` |
| `IA_MODEL` | Nombre del modelo | `llama3` |
| `DB_HOST` | Host de PostgreSQL | `localhost` |
| `DB_NAME` | Nombre de la base de datos | `notas_db` |
| `DB_USER` | Usuario de PostgreSQL | `postgres` |
| `DB_PASSWORD` | Contraseña de PostgreSQL | `1234` |

## Módulos del Backend

### `backend/main.py`
Punto de entrada de la aplicación. Configura CORS e incluye los routers.

### `backend/config.py`
Centraliza todas las configuraciones usando variables de entorno.

### `backend/database.py`
Maneja la conexión a PostgreSQL con helpers reutilizables para ejecutar consultas.

### `backend/schemas.py`
Define los modelos Pydantic para validación de datos de entrada y salida.

### `backend/routes/`
Define los endpoints HTTP (controladores). Cada archivo agrupa rutas relacionadas.

### `backend/services/`
Contiene la lógica de negocio. Separa la lógica de los controladores para mejor mantenibilidad.
