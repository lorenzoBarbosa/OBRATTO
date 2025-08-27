from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Rota para cadastrar promoção
@router.get("/fornecedor/promocoes/cadastrar")
async def cadastrar_promocao(request: Request):
    return templates.TemplateResponse("fornecedor/promocao/cadastrar_promocoes.html", {"request": request})

# Rota para alterar promoção
@router.get("/fornecedor/promocoes/alterar")
async def alterar_promocao(request: Request):
    return templates.TemplateResponse("fornecedor/promocaoalterar_promocoes.html", {"request": request})

# Rota para listar todas promoções
@router.get("/fornecedor/promocoes")
async def listar_promocoes(request: Request):
    return templates.TemplateResponse("fornecedor/promocao/promocoes.html", {"request": request})

# Rota para confirmar exclusão de promoção
@router.get("/fornecedor/promocoes/confirmar_exclusao")
async def confirmar_exclusao_promocao(request: Request):
    return templates.TemplateResponse("fornecedor/promocao/confirmar_exclusao_promocao.html", {"request": request})
