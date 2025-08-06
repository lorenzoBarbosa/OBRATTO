from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.plano import plano_repo


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/plano/{id}")
async def get_plano(request: Request, id: int):
    plano = plano_repo.obter_plano_por_id(id)
    return templates.TemplateResponse("plano.html", {"request": request, "plano": plano})