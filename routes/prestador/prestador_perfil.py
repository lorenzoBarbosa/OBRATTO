from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates
from fastapi.templating import Jinja2Templates


# Tudo funcionando corretamente!

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Rota para página inicial do Prestador
@router.get("/")
async def home_prestador(request: Request):
    return templates.TemplateResponse("prestador/home.html", {"request": request})

# Rota para painel do Prestador
@router.get("/painel")
async def painel_prestador(request: Request):
    return templates.TemplateResponse("prestador/perfil/painel.html", {"request": request})

@router.get("/cadastro")
async def exibir_cadastro_fornecedor(request: Request):
    return templates.TemplateResponse("prestador/perfil/prestador_cadastro.html", {"request": request})

# Visualizar perfil do fornecedor
@router.get("/perfil")
async def exibir_perfil_prestador(request: Request):
    return templates.TemplateResponse("prestador/perfil/perfil.html", {"request": request})

# Editar perfil
@router.get("/editar")
async def editar_perfil_prestador(request: Request):
    return templates.TemplateResponse("prestador/perfil/editar.html", {"request": request})

# Excluir perfil
@router.get("/excluir")
async def excluir_perfil_prestador(request: Request):
    return templates.TemplateResponse("prestador/perfil/excluir.html", {"request": request})

@router.get("/perfil_publico")
async def exibir_perfil_publico(request: Request):
    return templates.TemplateResponse("prestador/perfil/perfil_publico.html", {"request": request})

