
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse("publico/home.html", {"request": request})

@router.get("/escolha_cadastro")
async def mostrar_escolha_cadastro(request: Request):
    return templates.TemplateResponse("publico/escolha_cadastro.html", {"request": request})