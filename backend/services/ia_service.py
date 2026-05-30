import httpx
from backend.config import IA_API_URL, IA_API_KEY, IA_MODEL


def mejorar_texto(texto: str) -> str:
    prompt = (
        "Eres un asistente que mejora textos en español. "
        "Corrige la ortografía, gramática y redacción del siguiente texto, "
        "haciéndolo más claro y profesional. Devuelve solo el texto mejorado, sin explicaciones.\n\n"
        f"Texto: {texto}"
    )

    headers = {
        "Content-Type": "application/json",
    }
    if IA_API_KEY:
        headers["Authorization"] = f"Bearer {IA_API_KEY}"

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
    except Exception as e:
        raise Exception(f"Error al comunicarse con la IA: {e}")
