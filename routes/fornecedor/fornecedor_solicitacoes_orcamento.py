from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from utils.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Rota GET para exibir solicitações recebidas
@router.get("/solicitacoes_recebidas")
async def solicitacoes_recebidas(request: Request):
	return templates.TemplateResponse("fornecedor/orcamentos/solicitacoes_recebidas.html", {"request": request})

@router.get("/listar")
@requer_autenticacao(['fornecedor'])
async def listar_solicitacoes(request: Request):
	return {"message": "Listar solicitações"}

@router.get("/detalhar")
@requer_autenticacao(['fornecedor'])
async def detalhar_solicitacao(request: Request):
	return {"message": "Detalhar solicitação"}

@router.post("/responder")
@requer_autenticacao(['fornecedor'])
async def responder_solicitacao(request: Request):
	return {"message": "Responder solicitação"}


