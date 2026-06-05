import httpx
from backend.config import IA_API_URL, IA_API_KEY, IA_MODEL


def mejorar_texto(texto: str) -> str:
    if not IA_API_KEY:
        raise Exception(
            "IA_API_KEY no configurada. "
            "Establece la variable de entorno IA_API_KEY con tu clave de Google AI Studio "
            "o configura Ollama localmente (ver README)."
        )

    prompt = (
        "Eres un asistente que mejora textos en español. "
        "Corrige la ortografía, gramática y redacción del siguiente texto, "
        "haciéndolo más claro y profesional. Devuelve solo el texto mejorado, sin explicaciones.\n\n"
        f"Texto: {texto}"
    )

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {IA_API_KEY}",
    }

    payload = {
        "model": IA_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 500,
    }

    try:
        response = httpx.post(IA_API_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        texto_mejorado = data["choices"][0]["message"]["content"].strip()
        return texto_mejorado
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 401:
            raise Exception("Error de autenticación: la clave de IA no es válida. Verifica tu IA_API_KEY.")
        elif status == 429:
            raise Exception("Límite de peticiones de la IA alcanzado. Intenta de nuevo más tarde.")
        else:
            raise Exception(f"Error HTTP {status} al comunicarse con la IA: {e.response.text}")
    except httpx.ConnectError:
        raise Exception(
            f"No se pudo conectar con {IA_API_URL}. "
            "Verifica que la URL sea correcta y que tengas conexión a internet."
        )
    except httpx.TimeoutException:
        raise Exception("La IA no respondió a tiempo. Intenta de nuevo.")
    except KeyError:
        raise Exception("Respuesta inesperada de la IA. Verifica que el modelo y la URL sean correctos.")
    except Exception as e:
        raise Exception(f"Error al comunicarse con la IA: {e}")
