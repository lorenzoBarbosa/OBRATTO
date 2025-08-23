from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Rota GET para moderar anúncios
@router.get("/administrador/moderar_anuncios")
async def moderar_anuncios(request: Request):
	return templates.TemplateResponse("administrador/moderar_anuncios.html", {"request": request})
