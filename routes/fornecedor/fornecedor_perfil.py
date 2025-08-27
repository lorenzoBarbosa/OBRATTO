from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from data.fornecedor.fornecedor_model import Fornecedor
from data.fornecedor import fornecedor_repo
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Adicionar middleware de sessão (no main.py, exemplo):
# app.add_middleware(SessionMiddleware, secret_key="sua_chave_secreta")

# Cadastro do fornecedor
@router.post("/fornecedor/perfil/cadastrar")
async def cadastrar_fornecedor(request: Request, nome: str = Form(...), email: str = Form(...), senha: str = Form(...), razao_social: str = Form(...)):
    fornecedor = Fornecedor(id=None, nome=nome, email=email, senha=senha, razao_social=razao_social)
    fornecedor_repo.inserir_fornecedor(fornecedor)
    return templates.TemplateResponse("fornecedor/perfil.html", {"request": request, "mensagem": "Fornecedor cadastrado com sucesso", "fornecedor": fornecedor})

# Visualizar perfil do fornecedor
@router.get("/fornecedor/perfil/{id}")
async def visualizar_perfil(request: Request, id: int):
    fornecedor = fornecedor_repo.obter_fornecedor_por_id(id)
    return templates.TemplateResponse("fornecedor/perfil.html", {"request": request, "fornecedor": fornecedor})

# Editar perfil do fornecedor
@router.post("/fornecedor/perfil/editar/{id}")
async def editar_perfil(request: Request, id: int, nome: str = Form(...), email: str = Form(...), razao_social: str = Form(...)):
    fornecedor = fornecedor_repo.obter_fornecedor_por_id(id)
    if fornecedor:
        fornecedor.nome = nome
        fornecedor.email = email
        fornecedor.razao_social = razao_social
        fornecedor_repo.atualizar_fornecedor(fornecedor)
        mensagem = "Perfil atualizado com sucesso"
    else:
        mensagem = "Fornecedor não encontrado"
    return templates.TemplateResponse("fornecedor/perfil.html", {"request": request, "fornecedor": fornecedor, "mensagem": mensagem})

# Excluir perfil do fornecedor
@router.post("/fornecedor/perfil/excluir/{id}")
async def excluir_perfil(request: Request, id: int):
    fornecedor = fornecedor_repo.obter_fornecedor_por_id(id)
    if fornecedor:
        fornecedor_repo.deletar_fornecedor(id)
        mensagem = "Perfil excluído com sucesso"
        fornecedor = None
    else:
        mensagem = "Fornecedor não encontrado"
    return templates.TemplateResponse("fornecedor/perfil.html", {"request": request, "fornecedor": fornecedor, "mensagem": mensagem})

# Alterar senha do fornecedor
@router.post("/fornecedor/perfil/alterar_senha/{id}")
async def alterar_senha(request: Request, id: int, senha_nova: str = Form(...)):
    fornecedor = fornecedor_repo.obter_fornecedor_por_id(id)
    if fornecedor:
        fornecedor.senha = senha_nova
        fornecedor_repo.atualizar_fornecedor(fornecedor)
        mensagem = "Senha alterada com sucesso"
    else:
        mensagem = "Fornecedor não encontrado"
    return templates.TemplateResponse("fornecedor/perfil.html", {"request": request, "fornecedor": fornecedor, "mensagem": mensagem})

# Rota GET para exibir o perfil do fornecedor
@router.get("/fornecedor/perfil_publico")
async def exibir_perfil(request: Request):
    return templates.TemplateResponse("fornecedor/perfil.html", {"request": request})

@router.get("/fornecedor/conta")
async def exibir_conta(request: Request):
    return templates.TemplateResponse("fornecedor/conta.html", {"request": request})

# Rota GET para exibir o formulário de login
@router.get("/fornecedor/login")
async def mostrar_login(request: Request):
    return templates.TemplateResponse("fornecedor/login.html", {"request": request})

# Rota POST para processar login
@router.post("/fornecedor/login")
async def processar_login(request: Request, email: str = Form(...), senha: str = Form(...)):
    fornecedores = fornecedor_repo.obter_fornecedor()
    fornecedor = next((f for f in fornecedores if f.email == email and f.senha == senha), None)
    if fornecedor:
        request.session["fornecedor_id"] = fornecedor.id
        return RedirectResponse(url=f"/fornecedor/perfil/{fornecedor.id}", status_code=302)
    else:
        mensagem = "E-mail ou senha inválidos"
        return templates.TemplateResponse("fornecedor/login.html", {"request": request, "mensagem": mensagem})
