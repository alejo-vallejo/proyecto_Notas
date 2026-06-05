import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_NAME", "notas_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "1234"),
}

IA_API_URL = os.getenv("IA_API_URL", "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions")
IA_API_KEY = os.getenv("IA_API_KEY", "")
IA_MODEL = os.getenv("IA_MODEL", "gemini-2.0-flash")
