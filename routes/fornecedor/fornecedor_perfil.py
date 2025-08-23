from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Rota GET para exibir o perfil do fornecedor
@router.get("/fornecedor/perfil_publico")
async def exibir_perfil(request: Request):
	return templates.TemplateResponse("fornecedor/perfil.html", {"request": request})


@router.get("/fornecedor/conta")
async def exibir_conta(request: Request):
	return templates.TemplateResponse("fornecedor/conta.html", {"request": request})
