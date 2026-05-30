from backend.database import execute_query


def get_all_notas():
    return execute_query(
        "SELECT * FROM notas ORDER BY id DESC",
        fetch_all=True
    )


def get_nota_by_id(nota_id: int):
    return execute_query(
        "SELECT * FROM notas WHERE id = %s",
        (nota_id,),
        fetch_one=True
    )


def create_nota(titulo: str, contenido: str, usuario_id: int = 1):
    return execute_query(
        """
        INSERT INTO notas (titulo, contenido, usuario_id)
        VALUES (%s, %s, %s)
        RETURNING *
        """,
        (titulo, contenido, usuario_id),
        fetch_one=True,
        commit=True
    )


def update_nota(nota_id: int, titulo: str = None, contenido: str = None):
    fields = []
    values = []
    if titulo is not None:
        fields.append("titulo = %s")
        values.append(titulo)
    if contenido is not None:
        fields.append("contenido = %s")
        values.append(contenido)
    if not fields:
        return None
    values.append(nota_id)
    query = f"UPDATE notas SET {', '.join(fields)} WHERE id = %s RETURNING *"
    return execute_query(query, tuple(values), fetch_one=True, commit=True)


def delete_nota(nota_id: int):
    return execute_query(
        "DELETE FROM notas WHERE id = %s RETURNING id",
        (nota_id,),
        fetch_one=True,
        commit=True
    )
