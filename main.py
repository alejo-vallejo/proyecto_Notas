from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#  CONEXIÓN A BASE DE DATOS
def get_db():
    return psycopg2.connect(
        host="localhost",
        database="notas_db",
        user="postgres",
        password="1234"
    )

#  1. ENDPOINT PRINCIPAL
@app.get("/")
def inicio():
    return {"mensaje": "API de notas funcionando con PostgreSQL"}

#  2. OBTENER NOTAS (READ)
@app.get("/notas")
def obtener_notas():
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute("SELECT * FROM notas ORDER BY id DESC")
        notas = cur.fetchall()
        return notas

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cur.close()
        conn.close()

#  3. CREAR NOTA (CREATE)
@app.post("/notas")
def crear_nota(nota: dict):
    if not nota.get("titulo") or not nota.get("contenido"):
        raise HTTPException(status_code=400, detail="Faltan datos")

    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute(
            """
            INSERT INTO notas (titulo, contenido, usuario_id)
            VALUES (%s, %s, %s)
            RETURNING *
            """,
            (nota["titulo"], nota["contenido"], 1)
        )

        nueva_nota = cur.fetchone()
        conn.commit()
        return nueva_nota

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cur.close()
        conn.close()

#  4. ACTUALIZAR NOTA (UPDATE)
@app.put("/notas/{id}")
def actualizar_nota(id: int, nota: dict):
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute(
            """
            UPDATE notas
            SET titulo = %s, contenido = %s
            WHERE id = %s
            RETURNING *
            """,
            (nota.get("titulo"), nota.get("contenido"), id)
        )

        actualizada = cur.fetchone()

        if not actualizada:
            raise HTTPException(status_code=404, detail="Nota no encontrada")

        conn.commit()
        return actualizada

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cur.close()
        conn.close()

#  5. ELIMINAR NOTA (DELETE)
@app.delete("/notas/{id}")
def eliminar_nota(id: int):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM notas WHERE id = %s RETURNING id", (id,))
        eliminado = cur.fetchone()

        if not eliminado:
            raise HTTPException(status_code=404, detail="Nota no encontrada")

        conn.commit()
        return {"mensaje": "Nota eliminada correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cur.close()
        conn.close()