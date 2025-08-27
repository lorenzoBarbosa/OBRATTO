from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates

router = APIRouter()

# Rota para assinatura de plano do prestador
@router.get("/assinatura")
async def assinatura_prestador(request: Request):
    return templates.TemplateResponse("prestador/assinatura.html", {"request": request})

# Rota para editar assinatura do prestador
@router.get("/assinatura/editar/")
async def editar_assinatura(request: Request):
    return templates.TemplateResponse("prestador/assinatura_editar.html", {"request": request})

# Rota para remover assinatura do prestador
@router.get("/assinatura/remover/")
async def remover_assinatura(request: Request):
    return templates.TemplateResponse("prestador/assinatura_cancelar.html", {"request": request})
