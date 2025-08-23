

# Rotas de planos do fornecedor
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse
from data.plano.plano_model import Plano
from data.plano import plano_repo
from data.inscricaoplano.inscricao_plano_model import InscricaoPlano
from data.inscricaoplano import inscricao_plano_repo
from data.pagamento.pagamento_model import Pagamento
from data.pagamento import pagamento_repo
from data.pagamento.pagamento_repo import PagamentoRepository
from utils.mercadopago_config import mp_config

mercadopago_config = mp_config
router = APIRouter()
templates = Jinja2Templates(directory="templates")



# Listar planos disponíveis
@router.get("/fornecedor/planos/listar")
async def listar_planos(request: Request):
    try:
        planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=10)
        return templates.TemplateResponse("fornecedor/listar_planos.html", {"request": request, "planos": planos})
    except Exception as e:
        return templates.TemplateResponse("fornecedor/listar_planos.html", {"request": request, "planos": [], "mensagem": f"Erro ao carregar planos: {str(e)}"})




# Mostrar formulário de alteração de plano
@router.get("/fornecedor/planos/alterar")
async def mostrar_alterar_plano(request: Request):
    try:
        planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
        plano_atual = None
        return templates.TemplateResponse("fornecedor/alterar_plano.html", {
            "request": request, "planos": planos, "plano_atual": plano_atual
        })
    except Exception as e:
        return templates.TemplateResponse("fornecedor/alterar_plano.html", {"request": request, "planos": [], "mensagem": f"Erro: {str(e)}"})



# Processar alteração de plano
@router.post("/fornecedor/planos/alterar")
async def alterar_plano(request: Request, id_plano: int = Form(...), id_fornecedor: int = Form(...)):
    try:
        plano = plano_repo.obter_plano_por_id(id_plano)
        if plano:
            planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
            return templates.TemplateResponse("fornecedor/listar_planos.html", {
                "request": request, "planos": planos, "mensagem": f"Plano alterado para: {plano.nome_plano}"
            })
        else:
            planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
            return templates.TemplateResponse("fornecedor/alterar_plano.html", {
                "request": request, "planos": planos, "mensagem": "Plano não encontrado"
            })
    except Exception as e:
        planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
        return templates.TemplateResponse("fornecedor/alterar_plano.html", {
            "request": request, "planos": planos, "mensagem": f"Erro ao alterar plano: {str(e)}"
        })



# Mostrar confirmação de cancelamento de plano
@router.get("/fornecedor/planos/cancelar")
async def mostrar_cancelar_plano(request: Request):
    try:
        plano_atual = None
        return templates.TemplateResponse("fornecedor/cancelar_plano.html", {
            "request": request, "plano_atual": plano_atual
        })
    except Exception as e:
        return templates.TemplateResponse("fornecedor/cancelar_plano.html", {
            "request": request, "mensagem": f"Erro: {str(e)}"
        })



# Processar cancelamento de plano
@router.post("/fornecedor/planos/cancelar")
async def cancelar_plano(request: Request, id_fornecedor: int = Form(...), confirmacao: str = Form(...)):
    try:
        if confirmacao.lower() == "confirmar":
            return templates.TemplateResponse("fornecedor/cancelar_plano.html", {
                "request": request, "mensagem": "Plano cancelado com sucesso!", "cancelado": True
            })
        else:
            return templates.TemplateResponse("fornecedor/cancelar_plano.html", {
                "request": request, "mensagem": "Cancelamento não confirmado. Digite 'confirmar' para cancelar o plano."
            })
    except Exception as e:
        return templates.TemplateResponse("fornecedor/cancelar_plano.html", {
            "request": request, "mensagem": f"Erro ao cancelar plano: {str(e)}"
        })




# Mostrar formulário de renovação de plano
@router.get("/fornecedor/planos/renovar")
async def mostrar_renovar_plano(request: Request):
    try:
        planos_disponiveis = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
        plano_atual = planos_disponiveis[0] if planos_disponiveis else None
        return templates.TemplateResponse("fornecedor/renovar_plano.html", {
            "request": request, "planos_disponiveis": planos_disponiveis, "plano_atual": plano_atual
        })
    except Exception as e:
        return templates.TemplateResponse("fornecedor/renovar_plano.html", {
            "request": request, "planos_disponiveis": [], "mensagem": f"Erro: {str(e)}"
        })




# Processar renovação de plano
@router.post("/fornecedor/planos/renovar")
async def renovar_plano(request: Request, plano_id: int = Form(...)):
    try:
        plano = plano_repo.obter_plano_por_id(plano_id)
        if plano:
            planos_disponiveis = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
            return templates.TemplateResponse("fornecedor/listar_planos.html", {
                "request": request, "planos": planos_disponiveis, "mensagem": f"Plano renovado com sucesso: {plano.nome_plano}"
            })
        else:
            planos_disponiveis = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
            return templates.TemplateResponse("fornecedor/renovar_plano.html", {
                "request": request, "planos_disponiveis": planos_disponiveis, "mensagem": "Plano não encontrado"
            })
    except Exception as e:
        planos_disponiveis = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
        return templates.TemplateResponse("fornecedor/renovar_plano.html", {
            "request": request, "planos_disponiveis": planos_disponiveis, "mensagem": f"Erro ao renovar plano: {str(e)}"
        })




# Mostrar formulário de assinatura de plano
@router.get("/fornecedor/planos/assinar")
async def mostrar_assinar_plano(request: Request):
    try:
        planos_disponiveis = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
        return templates.TemplateResponse("fornecedor/assinar_plano.html", {
            "request": request, "planos_disponiveis": planos_disponiveis
        })
    except Exception as e:
        return templates.TemplateResponse("fornecedor/assinar_plano.html", {
            "request": request, "planos_disponiveis": [], "mensagem": f"Erro: {str(e)}"
        })




# Processar assinatura de plano
@router.post("/fornecedor/planos/assinar")
async def assinar_plano(request: Request, plano_id: int = Form(...), id_fornecedor: int = Form(default=1)):
    try:
        plano = plano_repo.obter_plano_por_id(plano_id)
        if not plano:
            planos_disponiveis = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
            return templates.TemplateResponse("fornecedor/assinar_plano.html", {
                "request": request, "planos_disponiveis": planos_disponiveis, "mensagem": "Plano não encontrado"
            })
        pagamento_repo.criar_tabela_pagamento()
        preference_result = mp_config.create_preference(
            plano_id=plano.id_plano,
            plano_nome=plano.nome_plano,
            valor=plano.valor_mensal,
            fornecedor_id=id_fornecedor
        )
        if preference_result["success"]:
            pagamento = Pagamento(
                plano_id=plano.id_plano,
                fornecedor_id=id_fornecedor,
                mp_preference_id=preference_result["preference_id"],
                valor=plano.valor_mensal,
                status="pendente",
                external_reference=f"plano_{plano.id_plano}_fornecedor_{id_fornecedor}"
            )
            pagamento_id = pagamento_repo.inserir_pagamento(pagamento)
            if pagamento_id:
                return templates.TemplateResponse("fornecedor/processar_pagamento.html", {
                    "request": request,
                    "plano": plano,
                    "preference_id": preference_result["preference_id"],
                    "init_point": preference_result["init_point"],
                    "sandbox_init_point": preference_result["sandbox_init_point"],
                    "mp_public_key": mp_config.PUBLIC_KEY
                })
            else:
                planos_disponiveis = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
                return templates.TemplateResponse("fornecedor/assinar_plano.html", {
                    "request": request, "planos_disponiveis": planos_disponiveis, "mensagem": "Erro ao criar registro de pagamento"
                })
        else:
            planos_disponiveis = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
            return templates.TemplateResponse("fornecedor/assinar_plano.html", {
                "request": request, "planos_disponiveis": planos_disponiveis, "mensagem": f"Erro ao criar preferência de pagamento: {preference_result.get('error', 'Erro desconhecido')}"
            })
    except Exception as e:
        planos_disponiveis = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
        return templates.TemplateResponse("fornecedor/assinar_plano.html", {
            "request": request, "planos_disponiveis": planos_disponiveis, "mensagem": f"Erro ao processar assinatura: {str(e)}"
        })


# Callback de sucesso do Mercado Pago
@router.get("/fornecedor/planos/pagamento/sucesso")
async def pagamento_sucesso(request: Request, payment_id: str = None, status: str = None, external_reference: str = None):
    try:
        if payment_id:
            payment_info = mp_config.get_payment_info(payment_id)
            if payment_info.get("status") == "approved":
                pagamento_repo.atualizar_status_pagamento(
                    mp_payment_id=payment_id,
                    status="aprovado",
                    metodo_pagamento=payment_info.get("payment_method_id")
                )
                return templates.TemplateResponse("fornecedor/pagamento_sucesso.html", {
                    "request": request, "payment_info": payment_info, "mensagem": "Pagamento aprovado com sucesso! Seu plano está ativo."
                })
        return templates.TemplateResponse("fornecedor/pagamento_sucesso.html", {
            "request": request, "mensagem": "Pagamento processado com sucesso!"
        })
    except Exception as e:
        return templates.TemplateResponse("fornecedor/pagamento_erro.html", {
            "request": request, "mensagem": f"Erro ao processar pagamento: {str(e)}"
        })



# Callback de falha do Mercado Pago
@router.get("/fornecedor/planos/pagamento/falha")
async def pagamento_falha(request: Request):
    return templates.TemplateResponse("fornecedor/pagamento_erro.html", {
        "request": request, "mensagem": "Pagamento rejeitado ou cancelado. Tente novamente."
    })



# Callback de pagamento pendente
@router.get("/fornecedor/planos/pagamento/pendente")
async def pagamento_pendente(request: Request):
    return templates.TemplateResponse("fornecedor/pagamento_pendente.html", {
        "request": request, "mensagem": "Pagamento pendente de aprovação. Aguarde a confirmação."
    })



# Webhook do Mercado Pago
@router.post("/fornecedor/planos/webhook/mercadopago")
async def webhook_mercadopago(request: Request):
    try:
        notification_data = await request.json()
        result = mp_config.process_webhook(notification_data)
        if result["success"]:
            payment_info = result["payment_info"]
            payment_id = str(payment_info["id"])
            status = payment_info["status"]
            status_map = {
                "approved": "aprovado",
                "rejected": "rejeitado",
                "cancelled": "cancelado",
                "pending": "pendente"
            }
            local_status = status_map.get(status, "pendente")
            pagamento_repo.atualizar_status_pagamento(
                mp_payment_id=payment_id,
                status=local_status,
                metodo_pagamento=payment_info.get("payment_method_id")
            )
        return JSONResponse({"status": "ok"})
    except Exception as e:
        print(f"Erro no webhook: {e}")
        return JSONResponse({"status": "error", "message": str(e)})



# Verificar status de pagamento
@router.get("/status_pagamento/{payment_id}")
async def verificar_status_pagamento(payment_id: str):
    try:
        payment_info = mercadopago_config.get_payment_info(payment_id)
        if payment_info:
            pagamento_repo = PagamentoRepository()
            pagamento_repo.atualizar_status(payment_id, payment_info["status"])
            return {
                "status": payment_info["status"],
                "payment_id": payment_id,
                "transaction_amount": payment_info.get("transaction_amount"),
                "status_detail": payment_info.get("status_detail")
            }
        return {"status": "not_found", "message": "Pagamento não encontrado"}
    except Exception as e:
        print(f"Erro ao verificar status: {e}")
        return {"status": "error", "message": str(e)}




# Debug dos planos
@router.get("/fornecedor/planos/debug")
async def debug_planos(request: Request):
    try:
        from utils.db import get_database_info
        db_info = get_database_info()
        plano_repo.criar_tabela_plano()
        pagamento_repo.criar_tabela_pagamento()
        planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=10)
        debug_info = {
            "database_info": db_info,
            "tabela_criada": True,
            "total_planos": len(planos),
            "planos": [
                {
                    "id": p.id_plano,
                    "nome": p.nome_plano,
                    "valor": p.valor_mensal,
                    "tipo": p.tipo_plano,
                    "descricao": p.descricao
                } for p in planos
            ]
        }
        return {"debug": debug_info, "status": "ok"}
    except Exception as e:
        return {"error": str(e), "status": "error"}
