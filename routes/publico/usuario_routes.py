from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.usuario import usuario_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/usuario/{id}")
async def get_usuario(request: Request, id: int):
    usuario = usuario_repo.obter_usuario_por_id(id)
    return templates.TemplateResponse("usuario.html", {"request": request, "usuario": usuario})