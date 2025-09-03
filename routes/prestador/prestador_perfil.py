from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cadastro")
async def exibir_cadastro_fornecedor(request: Request):
    return templates.TemplateResponse("prestador/prestador_cadastro.html", {"request": request})

# Visualizar perfil do fornecedor
@router.get("/prestador/perfil")
async def exibir_perfil_prestador(request: Request):
    return templates.TemplatesResponse("prestador/prestador_perfil.html", {"request": Request})

# Editar perfil
@router.get("/prestador/editar")
async def editar_perfil_prestador(request: Request):
    return templates.TemplatesResponse("prestador/prestador_editar.html", {"request": Request})

# Excluir perfil
@router.get("/prestador/excluir")
async def excluir_perfil_prestador(request: Request):
    return templates.TemplatesResponse("prestador/prestador_excluir.html", {"request": Request})

@router.get("/perfil_publico/{id}")
async def exibir_perfil_publico(request: Request):
    return templates.TemplateResponse("prestador/perfil.html", {"request": request})


