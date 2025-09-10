from tempfile import template
from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/")
async def get_root(request: Request):    
    return template.TemplateResponse("publico/home.html", {"request": request})

@router.get("/escolha_cadastro")
async def mostrar_escolha_cadastro(request: Request):
    return template.TemplateResponse("publico/escolha_cadastro.html", {"request": request})