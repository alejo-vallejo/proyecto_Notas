from fastapi import APIRouter, HTTPException
from backend.schemas import IATextoRequest, IATextoResponse
from backend.services.ia_service import mejorar_texto

router = APIRouter(prefix="/ia", tags=["Inteligencia Artificial"])


@router.post("", response_model=IATextoResponse)
def mejorar_con_ia(request: IATextoRequest):
    if not request.texto or not request.texto.strip():
        raise HTTPException(status_code=400, detail="El texto no puede estar vacío")
    try:
        texto_mejorado = mejorar_texto(request.texto)
        return IATextoResponse(texto_mejorado=texto_mejorado)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
