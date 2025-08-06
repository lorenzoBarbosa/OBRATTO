from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.notificacao import notificacao_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/notificacao/{id}")
async def get_notificacao(request: Request, id: int):
    notificacao = notificacao_repo.obter_notificacao_por_id(id)
    return templates.TemplateResponse("notificacao.html", {"request": request, "notificacao": notificacao})