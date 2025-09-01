from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates
from data.fornecedor import fornecedor_repo
from data.inscricaoplano import inscricao_plano_repo
from data.plano import plano_repo

router = APIRouter()

# Rota para assinatura de plano do prestador
@router.get("/planos")
async def planos_prestador(request: Request):
    return templates.TemplateResponse("prestador/planos.html", {"request": request})


# Rota para editar plano do prestador
@router.get("/planos/editar/")
async def editar_assinatura(request: Request):
    return templates.TemplateResponse("prestador/planos_editar.html", {"request": request})


# Processar alteração de assinatura do prestador
@router.post("/editar")
async def alterar_assinatura(request: Request, id_fornecedor: int = Form(...), id_plano: int = Form(...)):
    try:
        assinatura_ativa = inscricao_plano_repo.obter_inscricao_plano_por_id(id_prestador=id_prestador)
        if not assinatura_ativa:
            return templates.TemplateResponse("prestador/planos e pagamentos/alterar_assinatura.html", {
                "request": request, "mensagem": "Você não possui plano ativo para alterar."
            })
        plano = plano_repo.obter_plano_por_id(id_plano)
        if plano:
            planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
            return templates.TemplateResponse("prestador/planos e pagamentos/listar_planos.html", {
                "request": request, "planos": planos, "mensagem": f"Plano alterado para: {plano.nome_plano}"
            })
        else:
            planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
            return templates.TemplateResponse("prestador/planos e pagamentos/alterar_plano.html", {
                "request": request, "planos": planos, "mensagem": "Plano não encontrado"
            })
    except Exception as e:
        planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
        return templates.TemplateResponse("prestador/planos e pagamentos/alterar_plano.html", {
            "request": request, "planos": planos, "mensagem": f"Erro ao alterar plano: {str(e)}"
        })


# Rota para cancelar plano do prestador
@router.get("/planos/cancelar/")
async def cancelar_assinatura(request: Request):
    return templates.TemplateResponse("prestador/planos_cancelar.html", {"request": request})


@router.post("/cancelar")
async def cancelar_plano(request: Request, id_prestador: int = Form(...), confirmacao: str = Form(...)):
    try:
        assinatura_ativa = inscricao_plano_repo.obter_inscricao_plano_por_id(id_prestador)
        if not assinatura_ativa:
            return templates.TemplateResponse("prestador/planos e pagamentos/cancelar_plano.html", {
                "request": request, "mensagem": "Você não possui assinatura ativa para cancelar."
            })
        if confirmacao.lower() == "confirmar":
          
            return templates.TemplateResponse("prestador/planos e pagamentos/cancelar_plano.html", {
                "request": request, "mensagem": "Plano cancelado com sucesso!", "cancelado": True
            })
        else:
            return templates.TemplateResponse("prestador/planos e pagamentos/cancelar_plano.html", {
                "request": request, "mensagem": "Cancelamento não confirmado. Digite 'confirmar' para cancelar o plano."
            })
    except Exception as e:
        return templates.TemplateResponse("prestador/planos e pagamentos/cancelar_plano.html", {
            "request": request, "mensagem": f"Erro ao cancelar plano: {str(e)}"
        })

