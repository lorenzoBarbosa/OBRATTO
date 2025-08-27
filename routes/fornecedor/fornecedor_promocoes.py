from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Rota para listar todas promoções
@router.get("/listar")
async def listar_promocoes(request: Request):
    return templates.TemplateResponse("fornecedor/promocao/promocoes.html", {"request": request})

# Rota para cadastrar promoção
@router.get("/cadastrar")
async def cadastrar_promocao(request: Request):
    return templates.TemplateResponse("fornecedor/promocao/cadastrar_promocoes.html", {"request": request})

# Rota para alterar promoção
@router.get("/alterar")
async def alterar_promocao(request: Request):
    return templates.TemplateResponse("fornecedor/promocaoalterar_promocoes.html", {"request": request})

# Rota para confirmar exclusão de promoção
@router.get("/confirmar_exclusao")
async def confirmar_exclusao_promocao(request: Request):
    return templates.TemplateResponse("fornecedor/promocao/confirmar_exclusao_promocao.html", {"request": request})
