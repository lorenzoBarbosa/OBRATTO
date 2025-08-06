from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.prestador import prestador_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/prestador/{id}")
async def get_prestador(request: Request, id: int):
    prestador = prestador_repo.obter_prestador_por_id(id)
    return templates.TemplateResponse("prestador.html", {"request": request, "prestador": prestador})