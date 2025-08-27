from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Rota GET para exibir solicitações recebidas
@router.get("/fornecedor/solicitacoes/recebidas")
async def solicitacoes_recebidas(request: Request):
	return templates.TemplateResponse("fornecedor/produtos/solicitacoes_recebidas.html", {"request": request})


