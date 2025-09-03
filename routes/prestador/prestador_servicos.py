from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates
from data.servico import servico_repo

router = APIRouter()

# Rota para listar serviços do Prestador 
@router.get("/servicos")
async def listar_servicos(request: Request, q: Optional[str] = None):
    return templates.TemplateResponse("prestador/servicos_listar.html", {"request": request})

# Rota para cadastrar novo serviço
@router.get("/servicos/novo")
async def form_novo_servico(request: Request):
    return templates.TemplateResponse("prestador/servico_form.html", {"request": request})


