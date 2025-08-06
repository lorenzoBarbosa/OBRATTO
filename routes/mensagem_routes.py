from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.mensagem import mensagem_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/mensagem/{id}")
async def get_mensagem(request: Request, id: int):
    mensagem = mensagem_repo.obter_mensagem_por_id(id)
    return templates.TemplateResponse("mensagem.html", {"request": request, "mensagem": mensagem})