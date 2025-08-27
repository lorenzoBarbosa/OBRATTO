from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_page(request: Request):
    return templates.TemplateResponse("cliente/home.html", { "request": request })

@router.get("/cadastro")
async def get_page(request: Request):
    return templates.TemplateResponse("cliente/cadastro.html", {"request": request})


