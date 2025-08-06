from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.orcamento import orcamento_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/orcamento/{id}")
async def get_orcamento(request: Request, id: int):
    orcamento = orcamento_repo.obter_orcamento_por_id(id)
    return templates.TemplateResponse("orcamento.html", {"request": request, "orcamento": orcamento})