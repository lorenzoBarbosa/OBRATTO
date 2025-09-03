from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates

router = APIRouter()


# Rota para contratações do prestador
@router.get("/contratacoess")
async def prestador_contratacoes(request: Request):
    return templates.TemplateResponse("prestador/contratacoes_listar.html", {"request": request})



