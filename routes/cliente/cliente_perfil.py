from typing import Optional
from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from data.cliente import cliente_repo
from data.cliente.cliente_model import Cliente
from utils.auth_decorator import requer_autenticacao
from utils.security import criar_hash_senha

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_page(request: Request):
    return templates.TemplateResponse("cliente/home.html", { "request": request })

# Visualizar perfil do cliente
@router.get("/perfil")
@requer_autenticacao(["cliente"])
async def exibir_perfil_cliente(request: Request):
    return templates.TemplateResponse("cliente/perfil/perfil.html", {"request": request})

# Editar perfil
@router.get("/editar")
@requer_autenticacao(["cliente"])
async def editar_perfil_cliente(request: Request):
    return templates.TemplateResponse("cliente/perfil/editar.html", {"request": request})


# Rota para processar o formulário de edição
@router.post("/editar")
@requer_autenticacao(["cliente"])
async def processar_edicao_perfil_cliente(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    telefone: str = Form(...),
    cpf_cnpj: str = Form(...),
    endereco: str = Form(...),
    data_cadastro: str = Form(...),
    genero: str = Form(...),
    data_nascimento: str = Form(...),
    tipo_usuario: str = "cliente",
    foto: Optional[str] = None,
    token_redefinicao: Optional[str] = None,
    data_token: Optional[str] = None
):
    return templates.TemplateResponse("cliente/editar.html", {"request": request})

# Excluir perfil
@router.get("/excluir")
@requer_autenticacao(["cliente"])
async def excluir_perfil_prestador(request: Request):
    return templates.TemplateResponse("cliente/excluir.html", {"request": request})

# Rota para processar a exclusão do perfil
@router.post("/excluir")
@requer_autenticacao(["cliente"])
async def processar_exclusao_perfil_cliente(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    telefone: str = Form(...),
    cpf_cnpj: str = Form(...),
    endereco: str = Form(...),
    data_cadastro: str = Form(...),
    genero: str = Form(...),
    data_nascimento: str = Form(...),
    tipo_usuario: str = "cliente",
    foto: Optional[str] = None,
    token_redefinicao: Optional[str] = None,
    data_token: Optional[str] = None
    ):
    return templates.TemplateResponse("cliente/excluir.html", {"request": request})
