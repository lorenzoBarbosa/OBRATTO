from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.administrador import administrador_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/administrador/{id}")
async def get_administrador(request: Request, id: int):
    administrador = administrador_repo.obter_administrador_por_id(id)
    return templates.TemplateResponse("administrador.html", {"request": request, "administrador": administrador})