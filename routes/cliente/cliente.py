from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/{id}")
async def get_cliente(request: Request, id: int):
    return templates.TemplateResponse("cliente.html", {"request": request, "cliente": "cliente"})

router = APIRouter(prefix="/cliente", tags=["Cliente"])

# Rota para Home do Cliente 
@router.get("/home_cliente/")
async def home_cliente(request: Request):
    return templates.TemplateResponse("cliente/home.html", {
        "request": request,
        "id_cliente": "id_cliente_logado",
        "pagina_ativa": "home"
    })

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
@router.get("/solicitacoes/")
async def cliente_solicitacoes(request: Request):
    return templates.TemplateResponse("cliente/solicitacoes.html", {
        "request": request,
        "solicitacoes": "solicitacoes",
        "id_cliente": "id_cliente_logado",
        "pagina_ativa": "solicitacoes"
    })

# Rota para pagarmento de contratação
@router.get("/pagar_contratacao/{id_contratacao}")
async def pagar_contratacao(request: Request, id_contratacao: int):
    return templates.TemplateResponse("cliente/pagar_contratacao.html", {
        "request": request,
        "id_contratacao": id_contratacao,
        "id_cliente": "id_cliente_logado",
        "pagina_ativa": "contratacoes"
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


