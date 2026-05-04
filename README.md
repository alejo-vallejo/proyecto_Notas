# Proyecto: Sistema de Notas

---

## Repositorio del proyecto

Link del repositorio público:
https://github.com/alejo-vallejo/proyecto_Notas.git

## Programas

postgres
fastapi
wsl
opencode

---

## Clonar el proyecto

Para descargar el proyecto en tu computador, ejecutar:

```bash
git clone https://github.com/alejo-vallejo/proyecto_Notas.git
cd proyecto_Notas
```

---

## Instalación de dependencias

Crear entorno virtual:

```bash
python3 -m venv venv
```

Activar entorno virtual:

```bash
source venv/bin/activate   
```

Instalar librerías necesarias:

```bash
pip install fastapi uvicorn psycopg2-binary
```

---

## Arrancar el backend

Con el entorno virtual activado, ejecutar:

```bash
fastapi dev main.py
```

El servidor se ejecuta en:
http://127.0.0.1:8000

---

## Arrancar el frontend

Entrar a la carpeta frontend:

```bash
cd frontend
```

Abrir los archivos en el navegador:

```bash
explorer.exe index.html
explorer.exe ver.html
```

---

## Cómo levantar la base de datos

Para que el sistema funcione correctamente, es necesario iniciar PostgreSQL y crear la base de datos.

### 1. Iniciar PostgreSQL

```bash
sudo service postgresql start
```

---

### 2. Entrar a PostgreSQL

```bash
sudo -u postgres psql
```

---

### 3. Crear la base de datos

```sql
CREATE DATABASE notas_db;
\c notas_db;
```

---

### 4. Crear tablas

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE notas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200),
    contenido TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_id INTEGER REFERENCES usuarios(id)
);
```

---

### 5. Insertar datos de prueba

```sql
INSERT INTO usuarios (nombre, password) VALUES
('Juan', '123'),
('Maria', '123'),
('Carlos', '123'),
('Ana', '123'),
('Luis', '123');
```

---

### 6. Verificar funcionamiento

```sql
SELECT * FROM notas;
```

Si la consulta muestra resultados, la base de datos está funcionando correctamente.

---

## Notas

* El CRUD completo está implementado en el backend.
* En el frontend solo se desarrollaron las funciones de crear y consultar notas.
* Es necesario que PostgreSQL esté activo para que el sistema funcione correctamente.

---
