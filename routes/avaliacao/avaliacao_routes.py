from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.avaliacao import avaliacao_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/avaliacao/{id}")
async def get_avaliacao(request: Request, id: int):
    avaliacao = avaliacao_repo.obter_avaliacao_por_id(id)
    return templates.TemplateResponse("avaliacao.html", {"request": request, "avaliacao": avaliacao})