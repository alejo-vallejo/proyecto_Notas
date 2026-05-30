import psycopg2
from psycopg2.extras import RealDictCursor
from backend.config import DATABASE_CONFIG


def get_connection():
    try:
        conn = psycopg2.connect(**DATABASE_CONFIG)
        return conn
    except psycopg2.OperationalError as e:
        raise Exception(f"Error de conexión a la base de datos: {e}")


def execute_query(query, params=None, fetch_one=False, fetch_all=False, commit=False):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute(query, params)
        result = None
        if fetch_one:
            result = cur.fetchone()
        elif fetch_all:
            result = cur.fetchall()
        if commit:
            conn.commit()
        return result
    except Exception as e:
        if commit:
            conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()
