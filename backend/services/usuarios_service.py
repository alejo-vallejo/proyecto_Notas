from backend.database import execute_query


def create_usuario(nombre: str, password: str):
    existing = execute_query(
        "SELECT id FROM usuarios WHERE nombre = %s",
        (nombre,),
        fetch_one=True
    )
    if existing:
        raise ValueError("El usuario ya existe")
    return execute_query(
        "INSERT INTO usuarios (nombre, password) VALUES (%s, %s) RETURNING id, nombre",
        (nombre, password),
        fetch_one=True,
        commit=True
    )


def authenticate(nombre: str, password: str):
    user = execute_query(
        "SELECT id, nombre FROM usuarios WHERE nombre = %s AND password = %s",
        (nombre, password),
        fetch_one=True
    )
    return user


def get_all_usuarios():
    return execute_query(
        "SELECT id, nombre FROM usuarios ORDER BY id",
        fetch_all=True
    )


def get_usuario_by_id(usuario_id: int):
    return execute_query(
        "SELECT id, nombre FROM usuarios WHERE id = %s",
        (usuario_id,),
        fetch_one=True
    )
