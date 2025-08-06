from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from data.cliente import cliente_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/{id}")
async def get_cliente(request: Request, id: int):
    cliente = cliente_repo.obter_cliente_por_id(id)
    return templates.TemplateResponse("cliente.html", {"request": request, "cliente": cliente})