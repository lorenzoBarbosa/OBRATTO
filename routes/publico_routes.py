# CRIADO POR MAROQUIO
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_root(request: Request):    
    return templates.TemplateResponse("publico/home.html", {"request": request})

@router.get("/login")
async def get_root(request: Request):    
    return templates.TemplateResponse("publico/login.html", {"request": request})

@router.get("/cadastro")
async def get_root(request: Request):    
    return templates.TemplateResponse("publico/cadastro.html", {"request": request})

@router.get("/catalogo")
async def get_root(request: Request):    
    return templates.TemplateResponse("publico/catalogo.html", {"request": request})

@router.get("/perfil")
async def get_root(request: Request):    
    return templates.TemplateResponse("publico/perfil.html", {"request": request})