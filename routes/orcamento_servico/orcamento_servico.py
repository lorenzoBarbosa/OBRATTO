from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.orcamentoservico import orcamento_servico_repo


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/orcamento_servico_servico/{id}")
async def get_orcamento_servico(request: Request, id: int):
    orcamento_servico = orcamento_servico_repo.obter_orcamento_servico_por_id(id)
    return templates.TemplateResponse("orcamento_servico.html", {"request": request, "orcamento_servico": orcamento_servico})