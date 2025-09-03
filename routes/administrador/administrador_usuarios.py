from fastapi import APIRouter, Request
from fastapi import Form
from fastapi import APIRouter, Form, Depends, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from data.administrador import administrador_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

administrador_usuarios = APIRouter()

# Rota para exibir o formulário de cadastro do administrador
@router.get("/cadastro")
async def exibir_cadastro_administrador(request: Request):
    return templates.TemplateResponse("administrador/cadastro_adm.html", {"request": request})

# Rota para cadastrar um novo administrador
@router.post("/cadastro")
async def cadastrar_administrador(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...)
):
    novo_adm = {
        "nome": nome,
        "email": email,
        "senha": senha 
    }
    administrador_repo.criar_administrador(novo_adm)
    return templates.TemplateResponse("admiistrador/cadastro_adm.html", {"request": request})

# Rota para home do administrador
@router.get("/home")
async def home_adm(request: Request):
    return templates.TemplateResponse("administrador/home_adm.html", {"request": request})

# Rota para lista de administradores
@router.get("/lista")
async def lista_adm(request: Request):
    return templates.TemplateResponse("administrador/moderar_adm/lista_adm.html", {"request": request})

# Rota para moderar administradores
@router.get("/moderar_administrador")
async def moderar_adm(request: Request):
    return templates.TemplateResponse("administrador/moderar_adm/moderar_adm.html", {"request": request})

# Rota para moderar fornecedores
@router.get("/moderar_fornecedor")
async def moderar_fornecedor(request: Request):
    return templates.TemplateResponse("administrador/moderar_fornecedor.html", {"request": request})

# Rota para moderar prestadores
@router.get("/moderar_prestador")
async def moderar_prestador(request: Request):
    return templates.TemplateResponse("administrador/moderar_prestador.html", {"request": request})

# Rota para remover administrador
@router.get("/remover")
async def remover_adm(request: Request):
    return templates.TemplateResponse("administrador/moderar_adm/remover_adm.html", {"request": request})

# Rota para remover um administrador
@router.post("/remover")
async def remover_administrador(request: Request, id: int = Form(...)):
    administrador_repo.remover_administrador_por_id(id)
    return templates.TemplateResponse("adm/administrador_remover.html", {"request": request})

# Rota dinâmica para buscar administrador por id
@router.get("/id/{id}")
async def get_administrador(request: Request, id: int):
    administrador = administrador_repo.obter_administrador_por_id(id)
    return templates.TemplateResponse("administrador.html", {"request": request, "administrador": administrador})

