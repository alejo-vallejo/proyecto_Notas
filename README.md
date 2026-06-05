# Sistema de Notas

API REST para gestión de notas personales con FastAPI, PostgreSQL e integración de Inteligencia Artificial.

## Tecnologías

- **Backend:** Python + FastAPI
- **Base de datos:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript vanilla
- **IA:** API compatible con OpenAI (Gemini, Ollama, OpenAI)

## Estructura del Proyecto

```
proyecto_notas/
├── backend/
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
│   ├── index.html            # Página de inicio / landing
│   ├── ver.html              # Listar, crear y eliminar notas
│   ├── editar.html           # Editar nota + Mejorar con IA
│   ├── login.html            # Inicio de sesión / registro
│   ├── css/
│   │   └── style.css         # Estilos globales (tema oscuro)
│   └── js/
│       └── app.js            # Cliente API y utilidades
├── database/
│   └── database.sql          # Esquema y datos de prueba
├── main.py                   # Punto de entrada (API + frontend estático)
├── docker-compose.yml        # Entorno PostgreSQL con Docker
├── requirements.txt
├── .env.example              # Plantilla de variables de entorno
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
python main.py
```

El servidor se ejecutará en: **http://127.0.0.1:8000**

Documentación interactiva: **http://127.0.0.1:8000/docs**

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

Copia el archivo de ejemplo y ajústalo:

```bash
cp .env.example .env
```

El sistema usa una API compatible con OpenAI. Por defecto usa **Google Gemini**.

#### Opción 1: Google Gemini (por defecto, gratuito)

1. Obtén tu API key gratuita en [Google AI Studio](https://aistudio.google.com/apikey)
2. Asígnala en el archivo `.env`:

```
IA_API_KEY=tu-api-key-de-gemini
```

Los valores por defecto ya apuntan a Gemini:
- `IA_API_URL`: `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions`
- `IA_MODEL`: `gemini-2.0-flash`

#### Opción 2: Ollama (local, gratuito, sin API key)

1. Instala Ollama desde [ollama.ai](https://ollama.ai)
2. Descarga un modelo: `ollama pull llama3`
3. Asegúrate que Ollama esté corriendo: `ollama serve`
4. Configura en `.env`:

```
IA_API_URL=http://localhost:11434/v1/chat/completions
IA_API_KEY=
IA_MODEL=llama3
```

#### Opción 3: OpenAI

```bash
IA_API_URL=https://api.openai.com/v1/chat/completions
IA_API_KEY=sk-tu-api-key
IA_MODEL=gpt-4o-mini
```

#### Variables de entorno

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| `IA_API_URL` | URL de la API de IA | `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions` |
| `IA_API_KEY` | API Key (requerida para Gemini/OpenAI) | `""` |
| `IA_MODEL` | Nombre del modelo | `gemini-2.0-flash` |
| `DB_HOST` | Host de PostgreSQL | `localhost` |
| `DB_NAME` | Nombre de la base de datos | `notas_db` |
| `DB_USER` | Usuario de PostgreSQL | `postgres` |
| `DB_PASSWORD` | Contraseña de PostgreSQL | `1234` |

## Módulos del Backend

### `main.py` (raíz)
Punto de entrada principal. Sirve el frontend estático e incluye todos los routers de la API.

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
