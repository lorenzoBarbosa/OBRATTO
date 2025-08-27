from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates

router = APIRouter()


# Rota para solicitações do prestador
@router.get("/solicitacoes")
async def prestador_solicitacoes(request: Request):
    return templates.TemplateResponse("prestador/solicitacoes_listar.html", {"request": request})

# Rota para responder a solicitação do prestador
@router.get("/solicitacoes/responder/{id_solicitacao}")
async def responder_solicitacao(request: Request, id_solicitacao: int):
    return templates.TemplateResponse("prestador/solicitacao_detalhes.html", {"request": request})

