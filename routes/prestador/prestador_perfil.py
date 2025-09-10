from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates
from fastapi.templating import Jinja2Templates

from data.cliente.cliente_model import Cliente
from data.prestador import prestador_repo
from data.prestador.prestador_model import Prestador
from utils.auth_decorator import criar_sessao
from utils.security import criar_hash_senha, verificar_senha


# Tudo funcionando corretamente!

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Rota para página inicial do Prestador
@router.get("/")
async def home_prestador(request: Request):
    return templates.TemplateResponse("prestador/home.html", {"request": request})

# Rota para painel do Prestador
@router.get("/painel")
async def painel_prestador(request: Request):
    return templates.TemplateResponse("prestador/perfil/painel.html", {"request": request})

# Rota para logout
@router.get("/logout")
async def logout_prestador(request: Request):
    return templates.TemplateResponse("prestador/perfil/prestador_logout.html", {"request": request})

# Rota para login
@router.get("/login")
async def exibir_login_prestador(request: Request):
    return templates.TemplateResponse("prestador/perfil/prestador_login.html", {"request": request})

# Rota para processar o formulário de login
@router.post("/login")
async def post_login(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...),
    redirect: str = Form(None)
):
    prestador = prestador_repo.obter_por_email(email)
    
    if not prestador or not verificar_senha(senha, prestador.senha):
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "erro": "Email ou senha inválidos"}
        )
    
    # Criar sessão
    prestador_dict = {
        "nome": prestador.nome,
        "email": prestador.email,
        "senha": prestador.senha,
        "cpf_cnpj": prestador.cpf_cnpj,
        "telefone": prestador.telefone,
        "endereco": prestador.endereco,
        "area_atuacao": prestador.area_atuacao,
        "razao_social": prestador.razao_social,
        "descricao_servicos": prestador.descricao_servicos,
        "data_cadastro": prestador.data_cadastro,
        "perfil": prestador.perfil,
        "foto": prestador.foto
    }
    criar_sessao(request, prestador_dict)
    
    # Redirecionar
    if redirect:
        return RedirectResponse(redirect, status.HTTP_303_SEE_OTHER)
    
    if prestador.perfil == "admin":
        return RedirectResponse("/admin", status.HTTP_303_SEE_OTHER)
    
    return RedirectResponse("/", status.HTTP_303_SEE_OTHER)

# Cadastro do fornecedor
@router.get("/cadastro")
async def exibir_cadastro_fornecedor(request: Request):
    return templates.TemplateResponse("prestador/perfil/prestador_cadastro.html", {"request": request})

# Rota para processar o formulário de cadastro
@router.post("/cadastro")
async def processar_cadastro_prestador(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    senha: str = Form(...),
    cpf_cnpj: str = Form(...),
    endereco: str = Form(...),
    area_atuacao: str = Form(...),
    razao_social: Optional[str] = Form(None),
    descricao_servicos: Optional[str] = Form(None)
):


    # Verificar se email já existe
    if prestador_repo.obter_por_email(email):
        return templates.TemplateResponse(
            "cadastro.html",
            {"request": request, "erro": "Email já cadastrado"}
        )
    
    # Criar hash da senha
    senha_hash = criar_hash_senha(senha)
    
    # Criar usuário
    prestador = Prestador(
        id=0,
        nome=nome,
        email=email,
        senha=senha_hash,
        perfil="cliente"
    )
    
    prestador_id = prestador_repo.inserir(prestador)
    
    # Se tiver CPF/telefone, inserir na tabela cliente
    # if cpf_cnpj and telefone:
    #     cliente = Cliente(
    #         # id=usuario_id,
    #         # cpf=cpf,
    #         # telefone=telefone
    #     )
    #     prestador_repo.inserir(cliente)
    
    return RedirectResponse("/login", status.HTTP_303_SEE_OTHER)


# Visualizar perfil do fornecedor
@router.get("/perfil")
async def exibir_perfil_prestador(request: Request):
    return templates.TemplateResponse("prestador/perfil/perfil.html", {"request": request})

# Editar perfil
@router.get("/editar")
async def editar_perfil_prestador(request: Request):
    return templates.TemplateResponse("prestador/perfil/editar.html", {"request": request})

# Rota para processar o formulário de edição
@router.post("/editar")
async def processar_edicao_perfil_prestador(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cpf_cnpj: str = Form(...),
    endereco: str = Form(...),
    area_atuacao: str = Form(...),
    razao_social: Optional[str] = Form(None),
    descricao_servicos: Optional[str] = Form(None)
):
    return templates.TemplateResponse("prestador/perfil/editar.html", {"request": request})

# Excluir perfil
@router.get("/excluir")
async def excluir_perfil_prestador(request: Request):
    return templates.TemplateResponse("prestador/perfil/excluir.html", {"request": request})

# Rota para processar a exclusão do perfil
@router.post("/excluir")
async def processar_exclusao_perfil_prestador(request: Request, 
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cpf_cnpj: str = Form(...),
    endereco: str = Form(...),
    area_atuacao: str = Form(...),
    razao_social: Optional[str] = Form(None),
    descricao_servicos: Optional[str] = Form(None)
    ):
    return templates.TemplateResponse("prestador/perfil/excluir.html", {"request": request})

@router.get("/perfil_publico")
async def exibir_perfil_publico(request: Request):
    return templates.TemplateResponse("prestador/perfil/perfil_publico.html", {"request": request})

