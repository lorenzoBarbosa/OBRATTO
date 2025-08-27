from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates
from routes.publico.publico_routes import orcamento_repo

router = APIRouter(prefix="/prestador", tags=["Prestador"])


# Rota para página inicial do Prestador
@router.get("/", response_class=HTMLResponse, name="home_prestador")
async def home_prestador(request: Request):
    return templates.TemplateResponse("prestador/home.html", {"request": request})

# Rota para painel do Prestador
@router.get("/", response_class=HTMLResponse, name="painel_prestador")
async def painel_prestador(request: Request):
    return templates.TemplateResponse("prestador/home/painel.html", {"request": request, "id_prestador": 1, "pagina_ativa": "painel"})

# Rota para listar serviços do Prestador 
@router.get("/servicos", response_class=HTMLResponse, name="listar_servicos")
async def listar_servicos(request: Request, q: Optional[str] = None):
    return templates.TemplateResponse("prestador/servico/servicos_listar.html", {"request": request, "servicos": "servicos", "q": q, "id_prestador": 1, "pagina_ativa": "servicos"})

# Rota para cadastrar novo serviço
@router.get("/servicos/novo", response_class=HTMLResponse, name="form_novo_servico")
async def form_novo_servico(request: Request):
    return templates.TemplateResponse("prestador/servico/servico_form.html", {"request": request, "acao": "novo", "id_prestador": 1, "pagina_ativa": "servicos"})

# Rota para editar serviço 
@router.get("/servicos/{id_servico}/editar", response_class=HTMLResponse, name="form_editar_servico")
async def form_editar_servico(request: Request, id_servico: int):
    return templates.TemplateResponse("prestador/servico/servico_form.html", {"request": request, "servico": "servico", "acao": "editar", "id_prestador": 1, "pagina_ativa": "servicos"})

# Rota para remover serviço
@router.get("/servicos/{id_servico}/remover/")
async def remover_servico(request: Request):
    return templates.TemplateResponse("prestador/servico/remover.html", {"request": request, "servico": "servico", "acao": "remover"})

# Rota para agenda do prestador
@router.get("/agenda", response_class=HTMLResponse, name="agenda_prestador")
async def agenda_prestador(request: Request):
    return templates.TemplateResponse("prestador/home/agenda.html", {"request": request, "id_prestador": 1, "pagina_ativa": "agenda"})

# Rota para assinatura de plano do prestador
@router.get("/assinatura", response_class=HTMLResponse, name="assinatura_prestador")
async def assinatura_prestador(request: Request):
    return templates.TemplateResponse("prestador/home/assinatura.html", {"request": request, "id_prestador": 1, "pagina_ativa": "assinatura"})

# Rota para editar assinatura do prestador
@router.get("/assinatura/editar/")
async def editar_assinatura(request: Request):
    return templates.TemplateResponse("prestador/home/assinatura_editar.html", {"request": request, "id_prestador": 1, "pagina_ativa": "assinatura"})

# Rota para remover assinatura do prestador
@router.get("/assinatura/remover/")
async def remover_assinatura(request: Request):
    return templates.TemplateResponse("prestador/home/remover.html", {"request": request, "acao": "remover", "id_prestador": 1, "pagina_ativa": "assinatura"})

# Rota para solicitações do prestador
@router.get("/solicitacoes/")
async def prestador_solicitacoes(request: Request):
    return templates.TemplateResponse("prestador/home/solicitacoes.html", {"request": request, "solicitacoes": "solicitacoes", "id_prestador": 1, "pagina_ativa": "solicitacoes"})

# Rota para responder a solicitação do prestador
@router.get("/solicitacoes/{id_solicitacao}/responder")
async def responder_solicitacao(request: Request, id_solicitacao: int):
    return templates.TemplateResponse("prestador/home/responder_solicitacao.html", {"request": request, "solicitacao": "solicitacao", "id_prestador": 1, "pagina_ativa": "solicitacoes"})

