from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.servico import servico_repo


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/servico/{id}")
async def get_servico(request: Request, id: int):
    servico = servico_repo.obter_servico_por_id(id)
    return templates.TemplateResponse("servico.html", {"request": request, "servico": servico})