from fastapi import APIRouter, Request, Form, status
from fastapi.responses import RedirectResponse
from config import templates
from data.inscricaoplano import inscricao_plano_repo

router = APIRouter()

# Tudo funcionando corretamente!!

#Meu plano
@router.get("/meu_plano")
async def exibir_meu_plano(request: Request):
    plano = {
        "nome": "Plano Pro",
        "validade": "30 dias",
        "status": "Ativo"
    }
    return templates.TemplateResponse("prestador/planos/meu_plano.html", {"request": request, "plano": plano})

#Página principal de planos
@router.get("/planos")
async def planos_prestador(request: Request):
    return templates.TemplateResponse("prestador/planos/planos.html", {"request": request})

#Assinar plano
@router.get("/assinar")
async def assinar_plano(request: Request):
    return templates.TemplateResponse("prestador/planos/assinar.html", {"request": request})

# Rota para processar o formulário de assinatura do plano
@router.post("/assinar")
async def processar_assinatura_plano(request: Request, 
    id_prestador: int = Form(...), 
    nome_plano: str = Form(...),
    valor_mensal: float = Form(...),
    limite_servicos: int = Form(...),
    tipo_plano: str = Form(...),
    descricao: str = Form(...)
    ):
    return templates.TemplateResponse("prestador/planos/assinar.html", {"request": request})

#Confirmar assinatura
@router.get("/confirmar/assinatura")
async def confirmar_assinatura(request: Request):
    return templates.TemplateResponse("prestador/planos/confirmar_assinatura.html", {"request": request})

#Editar plano
@router.get("/editar/plano")
async def exibir_formulario_edicao(request: Request, id_prestador: int):
    return templates.TemplateResponse("prestador/planos/editar.html", {"request": request, "id_prestador": id_prestador})

#Rota para processar o formulário de edição do plano
@router.post("/editar/plano")
async def processar_edicao_plano(request: Request, 
    id_prestador: int = Form(...), 
    nome_plano: str = Form(...),
    valor_mensal: float = Form(...),
    limite_servicos: int = Form(...),
    tipo_plano: str = Form(...),
    descricao: str = Form(...)
    ):
     return templates.TemplateResponse("prestador/planos/editar.html", {"request": request, "id_prestador": id_prestador})


#Renovar plano 
@router.get("/renovar")
async def exibir_pagina_renovacao(request: Request):
    return templates.TemplateResponse("prestador/planos/renovar.html", {"request": request})

#Cancelar plano 
@router.get("/cancelar/{plano_id}")
async def cancelar_plano(request: Request, plano_id: int):
    return templates.TemplateResponse(
        "prestador/planos/cancelar.html",
        {"request": request, "id": plano_id}
    )

# Rota para processar o cancelamento do plano
@router.post("/cancelar/plano")
async def processar_cancelamento_plano(request: Request, 
    id_prestador: int = Form(...), 
    nome_plano: str = Form(...),
    valor_mensal: float = Form(...),
    limite_servicos: int = Form(...),
    tipo_plano: str = Form(...),
    descricao: str = Form(...)
    ):
     return templates.TemplateResponse("prestador/planos/cancelar.html",{"request": request, "id": plano_id}
    )

#Confirmação de cancelamento
@router.get("/confirmar/cancelamento")
async def confirmar_cancelamento(request: Request):
    return templates.TemplateResponse("prestador/planos/confirmar_cancelamento.html", {"request": request})


