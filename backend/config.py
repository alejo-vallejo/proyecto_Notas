import os

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_NAME", "notas_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "1234"),
}

IA_API_URL = os.getenv("IA_API_URL", "http://localhost:11434/v1/chat/completions")
IA_API_KEY = os.getenv("IA_API_KEY", "")
IA_MODEL = os.getenv("IA_MODEL", "llama3")
