from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates

router = APIRouter()


# Tudo funcionando perfeitamente!!

# Rota para solicitações do prestador
@router.get("/minhas/solicitacoes")
async def prestador_solicitacoes(request: Request):
    return templates.TemplateResponse("prestador/solicitacoes/minhas_solicitacoes.html", {"request": request})


# Rota para visualizar detalhes da solicitação
@router.get("/detalhes/solicitacao/{id_solicitacao}")
async def responder_solicitacao(request: Request, id_solicitacao: int):
    return templates.TemplateResponse("prestador/solicitacoes/detalhes.html", {"request": request})


# Rota para responder a solicitação
@router.get("/responder/solicitacao/{id_solicitacao}")
async def aceitar_solicitacao(request: Request, id_solicitacao: int):
 return templates.TemplateResponse("prestador/solicitacoes/responder.html", {"request": request})