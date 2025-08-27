from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# Rota para lista de solicitações de contratação
@router.get("/solicitacoes/")
async def cliente_solicitacoes(request: Request):
    return templates.TemplateResponse("cliente/solicitacoes.html", {
        "request": request,
        "solicitacoes": "solicitacoes",
        "id_cliente": "id_cliente_logado",
        "pagina_ativa": "solicitacoes"
    })


# Rota para cancelar solicitação
@router.get("/cancelar_solicitacao/{id_solicitacao}")
async def cancelar_solicitacao(request: Request, id_solicitacao: int):
    return templates.TemplateResponse("cliente/cancelar_solicitacao.html", {
        "request": request,
        "id_solicitacao": id_solicitacao,
        "id_cliente": "id_cliente_logado",
        "pagina_ativa": "solicitacoes"
    })


