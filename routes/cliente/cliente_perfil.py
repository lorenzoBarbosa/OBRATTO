from typing import Optional
from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from data.cliente import cliente_repo
from data.cliente.cliente_model import Cliente
from utils.security import criar_hash_senha

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_page(request: Request):
    return templates.TemplateResponse("cliente/home.html", { "request": request })

# Rota para cadastro de cliente
@router.get("/cadastro")
async def get_page(request: Request):
    return templates.TemplateResponse("cliente/cadastro.html", {"request": request})

# Rota para processar o formulário de cadastro
@router.post("/cadastro")
async def post_cadastro(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    cpf_cnpj: str = Form(None),
    telefone: str = Form(None),
    endereco: str = Form(None),
    data_cadastro: str = Form(None),
    foto: str = Form(None),
    token_definicao: str = Form(None),
    data_token: str = Form(None),
    genero: str = Form(None),
    data_nascimento: str = Form(None),
    tipo_pessoa: str = Form("cliente")):
    # Verificar se email já existe
    if cliente_repo.obter_cliente_por_email(email):
        return templates.TemplateResponse(
            "cadastro.html",
            {"request": request, "erro": "Email já cadastrado"}
        )
    
    # Criar hash da senha
    senha_hash = criar_hash_senha(senha)
    
    # Criar usuário
    cliente = Cliente(
        id=0,
        nome=nome,
        email=email,
        senha=senha_hash,
        perfil="cliente"
    )
    
    cliente_id = cliente_repo.inserir(cliente)
    
    # Se tiver CPF/telefone, inserir na tabela cliente
    if cpf_cnpj and telefone:
        cliente = Cliente(
            id=cliente_id,
            nome=nome,
            email=email,
            senha=None,
            cpf_cnpj=cpf_cnpj,
            telefone=telefone,
            data_cadastro=data_cadastro,
            endereco=endereco,
            genero=genero,
            data_nascimento=data_nascimento,
            # tipo_usuario=tipo_usuario,
            foto=foto,
            # token_redefinicao=token_redefinicao,
            data_token=data_token,
        )
        cliente_repo.inserir(cliente)
    
    return RedirectResponse("/login", status.HTTP_303_SEE_OTHER)

# Rota para logout
@router.get("/logout")
async def logout_cliente(request: Request):
    return templates.TemplateResponse("cliente/perfil/cliente_logout.html", {"request": request})

# Rota para login
@router.get("/login")
async def exibir_login_cliente(request: Request):
    return templates.TemplateResponse("cliente/perfil/login.html", {"request": request})


# Visualizar perfil do cliente
@router.get("/perfil")
async def exibir_perfil_cliente(request: Request):
    return templates.TemplateResponse("cliente/perfil/perfil.html", {"request": request})

# Editar perfil
@router.get("/editar")
async def editar_perfil_cliente(request: Request):
    return templates.TemplateResponse("cliente/perfil/editar.html", {"request": request})


# Rota para processar o formulário de edição
@router.post("/editar")
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
async def excluir_perfil_prestador(request: Request):
    return templates.TemplateResponse("cliente/excluir.html", {"request": request})

# Rota para processar a exclusão do perfil
@router.post("/excluir")
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

@router.get("/perfil_publico")
async def exibir_perfil_publico(request: Request):
    return templates.TemplateResponse("cliente/perfil_publico.html", {"request": request})