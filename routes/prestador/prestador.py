from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates

router = APIRouter()

# Rota para página inicial do Prestador
@router.get("/")
async def home_prestador(request: Request):
    return templates.TemplateResponse("prestador/home.html", {"request": request})

# Rota para painel do Prestador
@router.get("/painel")
async def painel_prestador(request: Request):
    return templates.TemplateResponse("prestador/painel.html", {"request": request})


