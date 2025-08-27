from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# Rota para lista de contratações
@router.get("/contratacoes/")
async def cliente_contratacoes(request: Request):
    return templates.TemplateResponse("cliente/contratacoes.html", {
        "request": request,
        "contratacoes": "contratacoes",
        "id_cliente": "id_cliente_logado",
        "pagina_ativa": "contratacoes"
    })

# Rota para avaliar contratação
@router.get("/avaliar_contratacao/{id_contratacao}")
async def avaliar_contratacao(request: Request, id_contratacao: int):
    return templates.TemplateResponse("cliente/avaliar_contratacao.html", {
        "request": request,
        "id_contratacao": id_contratacao,
        "id_cliente": "id_cliente_logado",
        "pagina_ativa": "contratacoes"
    })

# Rota para lista de solicitações de contratação
@router.get("/solicitacoes de contratação/")
async def cliente_solicitacoes(request: Request):
    return templates.TemplateResponse("cliente/solicitacoes.html", {
        "request": request,
        "solicitacoes": "solicitacoes",
        "id_cliente": "id_cliente_logado",
        "pagina_ativa": "solicitacoes"
    })

# Rota para pagamento de contratação
@router.get("/pagar_contratacao/{id_contratacao}")
async def pagar_contratacao(request: Request, id_contratacao: int):
    return templates.TemplateResponse("cliente/pagar_contratacao.html", {
        "request": request,
        "id_contratacao": id_contratacao,
        "id_cliente": "id_cliente_logado",
        "pagina_ativa": "contratacoes"
    })


