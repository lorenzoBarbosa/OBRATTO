# CRIADO POR MAROQUIO
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from data.administrador import administrador_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# Rota para home do administrador
@router.get("/home")
async def home_adm(request: Request):
    return templates.TemplateResponse("administrador/home_adm.html", {"request": request})

# Rota para lista de administradores
@router.get("/lista")
async def lista_adm(request: Request):
    return templates.TemplateResponse("administrador/lista_adm.html", {"request": request})

# Rota para moderar administradores
@router.get("/moderar")
async def moderar_adm(request: Request):
    return templates.TemplateResponse("administrador/moderar_adm.html", {"request": request})

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
    return templates.TemplateResponse("administrador/remover_adm.html", {"request": request})

# Rota dinâmica para buscar administrador por id
@router.get("/id/{id}")
async def get_administrador(request: Request, id: int):
    administrador = administrador_repo.obter_administrador_por_id(id)
    return templates.TemplateResponse("administrador.html", {"request": request, "administrador": administrador})

#rota moderar_prestador não rodou 
#router get id