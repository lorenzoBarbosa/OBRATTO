from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse
from data.plano.plano_model import Plano
from data.plano import plano_repo
from data.inscricaoplano.inscricao_plano_model import InscricaoPlano
from data.inscricaoplano import inscricao_plano_repo
from data.pagamento.pagamento_model import Pagamento
from data.pagamento.pagamento_repo import PagamentoRepository
from data.cartao.cartao_model import CartaoCredito
from data.cartao.cartao_repo import CartaoRepository
from utils.mercadopago_config import mp_config

# Criar instância dos repositórios
pagamento_repo = PagamentoRepository()
cartao_repo = CartaoRepository()
mercadopago_config = mp_config
router = APIRouter()
templates = Jinja2Templates(directory="templates")



# Listar planos disponíveis
@router.get("/listar")
async def listar_planos(request: Request):
    planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=10)
    return templates.TemplateResponse("fornecedor/planos e pagamentos/listar_planos.html", {"request": request, "planos": planos})



# Mostrar formulário de alteração de plano
@router.get("/alterar")
async def mostrar_alterar_plano(request: Request, id_fornecedor: int = 1):
    assinatura_ativa = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
    plano_atual = None
    
    if assinatura_ativa:
        plano_atual = plano_repo.obter_plano_por_id(assinatura_ativa.id_plano)
    
    planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
    return templates.TemplateResponse("fornecedor/planos e pagamentos/alterar_plano.html", {
        "request": request, "planos": planos, "plano_atual": plano_atual, "id_fornecedor": id_fornecedor
    })


# Processar alteração de plano
@router.post("/alterar")
async def alterar_plano(request: Request, id_plano: int = Form(...)):
    id_fornecedor = 1  # Fixo para o fornecedor logado
    assinatura_ativa = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
    if not assinatura_ativa:
        planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
        return templates.TemplateResponse("fornecedor/planos e pagamentos/alterar_plano.html", {
            "request": request, "planos": planos, "mensagem": "Você não possui assinatura ativa para alterar."
        })
    
    plano_novo = plano_repo.obter_plano_por_id(id_plano)
    plano_atual = plano_repo.obter_plano_por_id(assinatura_ativa.id_plano)
    
    if plano_novo:
        # Verificar se há diferença de valor que requer pagamento
        if plano_novo.valor_mensal > plano_atual.valor_mensal:
            # Redirecionar para dados de pagamento se o novo plano é mais caro
            response = RedirectResponse(f"/fornecedor/planos/dados_pagamento?plano_id={id_plano}&id_fornecedor={id_fornecedor}&tipo=alteracao", status_code=303)
            return response
        else:
            # Atualizar diretamente se o novo plano é igual ou mais barato
            assinatura_ativa.id_plano = id_plano
            inscricao_plano_repo.atualizar_inscricao_plano(assinatura_ativa)
            response = RedirectResponse("/fornecedor/planos/listar", status_code=303)
            return response
    
    planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
    return templates.TemplateResponse("fornecedor/planos e pagamentos/alterar_plano.html", {
        "request": request, "planos": planos, "mensagem": "Erro ao alterar plano."
    })



# Mostrar confirmação de cancelamento de plano
@router.get("/cancelar")
async def mostrar_cancelar_plano(request: Request, id_fornecedor: int = 1):
    assinatura_ativa = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
    plano_atual = None
    
    if assinatura_ativa:
        plano_atual = plano_repo.obter_plano_por_id(assinatura_ativa.id_plano)
    
    return templates.TemplateResponse("fornecedor/planos e pagamentos/cancelar_plano.html", {
        "request": request, "plano_atual": plano_atual, "id_fornecedor": id_fornecedor
    })



# Processar cancelamento de plano
@router.post("/cancelar")
async def cancelar_plano(request: Request, id_fornecedor: int = Form(...)):
    assinatura_ativa = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
    if not assinatura_ativa:
        return templates.TemplateResponse("fornecedor/planos e pagamentos/cancelar_plano.html", {
            "request": request, "mensagem": "Você não possui assinatura ativa para cancelar."
        })
    
    plano_atual = plano_repo.obter_plano_por_id(assinatura_ativa.id_plano)
    return templates.TemplateResponse("fornecedor/planos e pagamentos/confirmacao_cancelamento_plano.html", {
        "request": request, "plano_atual": plano_atual, "id_fornecedor": id_fornecedor
    })


# Confirmar cancelamento de plano
@router.post("/confirmar_cancelamento")
async def confirmar_cancelamento_plano(request: Request, id_fornecedor: int = Form(...)):
    assinatura_ativa = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
    if not assinatura_ativa:
        return templates.TemplateResponse("fornecedor/planos e pagamentos/cancelar_plano.html", {
            "request": request, "mensagem": "Você não possui assinatura ativa para cancelar."
        })
    
    # Cancelar a assinatura ativa
    inscricao_plano_repo.deletar_inscricao_plano(assinatura_ativa.id_inscricao_plano)
    response = RedirectResponse("/fornecedor/planos/listar", status_code=303)
    return response




# Mostrar formulário de renovação de plano
@router.get("/renovar")
async def mostrar_renovar_plano(request: Request, id_fornecedor: int = 1):
    assinatura_ativa = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
    plano_atual = None
    
    if assinatura_ativa:
        plano_atual = plano_repo.obter_plano_por_id(assinatura_ativa.id_plano)
    
    return templates.TemplateResponse("fornecedor/planos e pagamentos/renovar_plano.html", {
        "request": request, "plano_atual": plano_atual, "id_fornecedor": id_fornecedor
    })




# Processar renovação de plano - redirecionar para dados de pagamento
@router.post("/renovar")
async def renovar_plano(request: Request, id_fornecedor: int = Form(...)):
    assinatura_ativa = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
    if not assinatura_ativa:
        return templates.TemplateResponse("fornecedor/planos e pagamentos/renovar_plano.html", {
            "request": request, "mensagem": "Você não possui assinatura ativa para renovar."
        })
    
    plano_atual = plano_repo.obter_plano_por_id(assinatura_ativa.id_plano)
    if plano_atual:
        # Redirecionar para dados de pagamento
        response = RedirectResponse(f"/fornecedor/planos/dados_pagamento?plano_id={plano_atual.id_plano}&id_fornecedor={id_fornecedor}&tipo=renovacao", status_code=303)
        return response
    
    return templates.TemplateResponse("fornecedor/planos e pagamentos/renovar_plano.html", {
        "request": request, "mensagem": "Erro ao renovar plano."
    })




# Mostrar formulário de assinatura de plano
@router.get("/assinar")
async def mostrar_assinar_plano(request: Request):
    planos_disponiveis = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
    return templates.TemplateResponse("fornecedor/planos e pagamentos/assinar_plano.html", {
        "request": request, "planos_disponiveis": planos_disponiveis
    })




# Processar assinatura de plano - redirecionar para dados de pagamento
@router.post("/assinar")
async def assinar_plano(request: Request, plano_id: int = Form(...), id_fornecedor: int = Form(default=1)):
    assinatura_ativa = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
    if assinatura_ativa:
        planos_disponiveis = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
        return templates.TemplateResponse("fornecedor/planos e pagamentos/assinar_plano.html", {
            "request": request, "planos_disponiveis": planos_disponiveis, "mensagem": "Você já possui uma assinatura ativa. Cancele antes de assinar outro plano."
        })
    
    plano = plano_repo.obter_plano_por_id(plano_id)
    if not plano:
        planos_disponiveis = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=20)
        return templates.TemplateResponse("fornecedor/planos e pagamentos/assinar_plano.html", {
            "request": request, "planos_disponiveis": planos_disponiveis, "mensagem": "Plano não encontrado"
        })
    
    # Redirecionar para dados de pagamento
    response = RedirectResponse(f"/fornecedor/planos/dados_pagamento?plano_id={plano_id}&id_fornecedor={id_fornecedor}&tipo=assinatura", status_code=303)
    return response


# Mostrar formulário de dados de pagamento
@router.get("/dados_pagamento")
async def mostrar_dados_pagamento(request: Request, plano_id: int, id_fornecedor: int = 1, tipo: str = "assinatura"):
    plano = plano_repo.obter_plano_por_id(plano_id)
    if not plano:
        response = RedirectResponse("/fornecedor/planos/listar", status_code=303)
        return response
    
    # Obter cartões salvos do fornecedor
    cartoes = cartao_repo.obter_cartoes_fornecedor(id_fornecedor)
    
    tipo_operacao_map = {
        "assinatura": "Nova Assinatura",
        "renovacao": "Renovação de Plano",
        "alteracao": "Alteração de Plano"
    }
    
    return templates.TemplateResponse("fornecedor/planos e pagamentos/dados_pagamento.html", {
        "request": request,
        "plano": plano,
        "id_fornecedor": id_fornecedor,
        "tipo_operacao": tipo_operacao_map.get(tipo, "Nova Assinatura"),
        "cartoes": cartoes
    })


# Processar pagamento
@router.post("/processar_pagamento")
async def processar_pagamento(
    request: Request,
    plano_id: int = Form(...),
    id_fornecedor: int = Form(...),
    tipo_operacao: str = Form(...),
    valor: float = Form(...),
    nome_completo: str = Form(...),
    cpf: str = Form(...),
    telefone: str = Form(...),
    email: str = Form(...),
    metodo_pagamento: str = Form(...),
    cartao_salvo: str = Form(default=""),
    numero_cartao: str = Form(default=""),
    validade: str = Form(default=""),
    cvv: str = Form(default=""),
    nome_cartao: str = Form(default=""),
    salvar_cartao: str = Form(default="")
):
    plano = plano_repo.obter_plano_por_id(plano_id)
    if not plano:
        cartoes = cartao_repo.obter_cartoes_fornecedor(id_fornecedor)
        return templates.TemplateResponse("fornecedor/planos e pagamentos/dados_pagamento.html", {
            "request": request, "mensagem": "Plano não encontrado.", "cartoes": cartoes
        })
    
    # Obter cartões para o template caso haja erro
    cartoes = cartao_repo.obter_cartoes_fornecedor(id_fornecedor)
    
    # Processar cartão
    cartao_usado = None
    if cartao_salvo:  # Usando cartão salvo
        try:
            cartao_usado = cartao_repo.obter_cartao_por_id(int(cartao_salvo))
            if not cartao_usado or cartao_usado.id_fornecedor != id_fornecedor:
                return templates.TemplateResponse("fornecedor/planos e pagamentos/dados_pagamento.html", {
                    "request": request, "plano": plano, "id_fornecedor": id_fornecedor,
                    "tipo_operacao": tipo_operacao, "cartoes": cartoes,
                    "mensagem": "Cartão selecionado não é válido."
                })
        except ValueError:
            return templates.TemplateResponse("fornecedor/planos e pagamentos/dados_pagamento.html", {
                "request": request, "plano": plano, "id_fornecedor": id_fornecedor,
                "tipo_operacao": tipo_operacao, "cartoes": cartoes,
                "mensagem": "Cartão selecionado não é válido."
            })
    else:  # Usando novo cartão
        if metodo_pagamento == "cartao":
            if not numero_cartao or not validade or not cvv or not nome_cartao:
                return templates.TemplateResponse("fornecedor/planos e pagamentos/dados_pagamento.html", {
                    "request": request, "plano": plano, "id_fornecedor": id_fornecedor,
                    "tipo_operacao": tipo_operacao, "cartoes": cartoes,
                    "mensagem": "Todos os campos do cartão são obrigatórios."
                })
            
            # Salvar cartão se solicitado
            if salvar_cartao == "true":
                try:
                    mes_vencimento, ano_vencimento = validade.split('/')
                    cartao_repo.criar_cartao_from_form(
                        id_fornecedor=id_fornecedor,
                        numero_cartao=numero_cartao.replace(' ', ''),
                        nome_titular=nome_cartao,
                        mes_vencimento=mes_vencimento,
                        ano_vencimento=ano_vencimento,
                        apelido=f"Cartão •••• {numero_cartao.replace(' ', '')[-4:]}",
                        principal=False
                    )
                except Exception as e:
                    print(f"Erro ao salvar cartão: {e}")
    
    # Processar diferentes tipos de operação
    from datetime import datetime
    
    if tipo_operacao == "Nova Assinatura":
        # Verificar se já tem assinatura ativa
        assinatura_ativa = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
        if assinatura_ativa:
            return templates.TemplateResponse("fornecedor/planos e pagamentos/dados_pagamento.html", {
                "request": request, "plano": plano, "id_fornecedor": id_fornecedor,
                "tipo_operacao": tipo_operacao, "mensagem": "Você já possui uma assinatura ativa."
            })
        
        # Criar nova inscrição
        nova_inscricao = InscricaoPlano(
            id_inscricao_plano=0,
            id_fornecedor=id_fornecedor,
            id_prestador=None,
            id_plano=plano_id
        )
        inscricao_id = inscricao_plano_repo.inserir_inscricao_plano(nova_inscricao)
        reference = f"assinatura_plano_{plano_id}_fornecedor_{id_fornecedor}"
        
    elif tipo_operacao == "Renovação de Plano":
        # Buscar assinatura ativa
        assinatura_ativa = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
        if not assinatura_ativa:
            return templates.TemplateResponse("fornecedor/planos e pagamentos/dados_pagamento.html", {
                "request": request, "plano": plano, "id_fornecedor": id_fornecedor,
                "tipo_operacao": tipo_operacao, "mensagem": "Nenhuma assinatura ativa encontrada."
            })
        inscricao_id = assinatura_ativa.id_inscricao_plano
        reference = f"renovacao_plano_{plano_id}_fornecedor_{id_fornecedor}"
        
    elif tipo_operacao == "Alteração de Plano":
        # Buscar assinatura ativa e atualizar o plano
        assinatura_ativa = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
        if not assinatura_ativa:
            return templates.TemplateResponse("fornecedor/planos e pagamentos/dados_pagamento.html", {
                "request": request, "plano": plano, "id_fornecedor": id_fornecedor,
                "tipo_operacao": tipo_operacao, "mensagem": "Nenhuma assinatura ativa encontrada."
            })
        
        # Atualizar o plano da assinatura
        assinatura_ativa.id_plano = plano_id
        inscricao_plano_repo.atualizar_inscricao_plano(assinatura_ativa)
        inscricao_id = assinatura_ativa.id_inscricao_plano
        reference = f"alteracao_plano_{plano_id}_fornecedor_{id_fornecedor}"
    
    # Criar registro de pagamento
    pagamento = Pagamento(
        id_pagamento=0,
        plano_id=plano_id,
        fornecedor_id=id_fornecedor,
        mp_payment_id=f"{metodo_pagamento}_payment_{inscricao_id}_{int(datetime.now().timestamp())}",
        mp_preference_id=f"{metodo_pagamento}_pref_{inscricao_id}_{int(datetime.now().timestamp())}",
        valor=valor,
        status="aprovado",  # Simulação: sempre aprova
        metodo_pagamento=f"{metodo_pagamento}_simulado",
        data_criacao=datetime.now().isoformat(),
        data_aprovacao=datetime.now().isoformat(),
        external_reference=reference
    )
    
    pagamento_inserido = pagamento_repo.inserir_pagamento(pagamento)
    
    if pagamento_inserido:
        return templates.TemplateResponse("fornecedor/planos e pagamentos/pagamento_sucesso.html", {
            "request": request,
            "plano": plano,
            "tipo_operacao": tipo_operacao,
            "metodo_pagamento": metodo_pagamento,
            "mensagem": f"{tipo_operacao} processada com sucesso! Pagamento via {metodo_pagamento.upper()} aprovado."
        })
    
    return templates.TemplateResponse("fornecedor/planos e pagamentos/dados_pagamento.html", {
        "request": request, "plano": plano, "id_fornecedor": id_fornecedor,
        "tipo_operacao": tipo_operacao, "mensagem": "Erro ao processar pagamento. Tente novamente."
    })


# Callback de sucesso do Mercado Pago
@router.get("/pagamento/sucesso")
async def pagamento_sucesso(request: Request, payment_id: str = None, status: str = None, external_reference: str = None):
    if payment_id:
        payment_info = mp_config.get_payment_info(payment_id)
        if payment_info.get("status") == "approved":
            pagamento_repo.atualizar_status_pagamento(
                mp_payment_id=payment_id,
                status="aprovado",
                metodo_pagamento=payment_info.get("payment_method_id")
            )
            return templates.TemplateResponse("fornecedor/planos e pagamentos/pagamento_sucesso.html", {
                "request": request, "payment_info": payment_info, "mensagem": "Pagamento aprovado com sucesso! Seu plano está ativo."
            })
    return templates.TemplateResponse("fornecedor/planos e pagamentos/pagamento_sucesso.html", {
        "request": request, "mensagem": "Pagamento processado com sucesso!"
    })



# Callback de falha do Mercado Pago
@router.get("/pagamento/falha")
async def pagamento_falha(request: Request):
    return templates.TemplateResponse("fornecedor/planos e pagamentos/pagamento_erro.html", {
        "request": request, "mensagem": "Pagamento rejeitado ou cancelado. Tente novamente."
    })



# Callback de pagamento pendente
@router.get("/pagamento/pendente")
async def pagamento_pendente(request: Request):
    return templates.TemplateResponse("fornecedor/planos e pagamentos/pagamento_pendente.html", {
        "request": request, "mensagem": "Pagamento pendente de aprovação. Aguarde a confirmação."
    })



# Visualizar plano atual (sem ID na URL)
@router.get("/meu_plano")
async def visualizar_meu_plano_atual(request: Request, id_fornecedor: int = 1):
    assinatura = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
    if assinatura:
        plano = plano_repo.obter_plano_por_id(assinatura.id_plano)
        return templates.TemplateResponse("fornecedor/planos e pagamentos/minha_assinatura.html", {
            "request": request,
            "assinatura": assinatura,
            "plano": plano,
            "id_fornecedor": id_fornecedor
        })
    return templates.TemplateResponse("fornecedor/planos e pagamentos/minha_assinatura.html", {
        "request": request,
        "mensagem": "Nenhuma assinatura ativa encontrada.",
        "id_fornecedor": id_fornecedor
    })


# Visualizar assinatura ativa do fornecedor
@router.get("/minha_assinatura/{id_fornecedor}")
async def visualizar_assinatura_ativa(request: Request, id_fornecedor: int):
    assinatura = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
    if assinatura:
        plano = plano_repo.obter_plano_por_id(assinatura.id_plano)
        return templates.TemplateResponse("fornecedor/planos e pagamentos/minha_assinatura.html", {
            "request": request,
            "assinatura": assinatura,
            "plano": plano,
            "id_fornecedor": id_fornecedor
        })
    return templates.TemplateResponse("fornecedor/planos e pagamentos/minha_assinatura.html", {
        "request": request,
        "mensagem": "Nenhuma assinatura ativa encontrada.",
        "id_fornecedor": id_fornecedor
    })


# ===== ROTAS DE GERENCIAMENTO DE CARTÕES =====

# Listar cartões do fornecedor
@router.get("/cartoes")
async def listar_cartoes(request: Request, id_fornecedor: int = 1):
    cartoes = cartao_repo.obter_cartoes_fornecedor(id_fornecedor)
    return templates.TemplateResponse("fornecedor/planos e pagamentos/meus_cartoes.html", {
        "request": request,
        "cartoes": cartoes,
        "id_fornecedor": id_fornecedor
    })


# Mostrar formulário para adicionar cartão
@router.get("/cartoes/adicionar")
async def mostrar_adicionar_cartao(request: Request, id_fornecedor: int = 1):
    return templates.TemplateResponse("fornecedor/planos e pagamentos/adicionar_cartao.html", {
        "request": request,
        "id_fornecedor": id_fornecedor
    })


# Processar adição de cartão
@router.post("/cartoes/adicionar")
async def adicionar_cartao(
    request: Request,
    id_fornecedor: int = Form(...),
    numero_cartao: str = Form(...),
    nome_titular: str = Form(...),
    mes_vencimento: str = Form(...),
    ano_vencimento: str = Form(...),
    apelido: str = Form(...),
    principal: str = Form(None)
):
    try:
        # Usar método conveniente do repository
        resultado = cartao_repo.criar_cartao_from_form(
            id_fornecedor=id_fornecedor,
            numero_cartao=numero_cartao,
            nome_titular=nome_titular,
            mes_vencimento=mes_vencimento,
            ano_vencimento=ano_vencimento,
            apelido=apelido,
            principal=(principal == "true")
        )
        
        if resultado:
            return RedirectResponse(url="/fornecedor/planos/cartoes", status_code=303)
        else:
            return templates.TemplateResponse("fornecedor/planos e pagamentos/adicionar_cartao.html", {
                "request": request,
                "id_fornecedor": id_fornecedor,
                "mensagem": "Erro ao salvar o cartão. Tente novamente."
            })
            
    except Exception as e:
        return templates.TemplateResponse("fornecedor/planos e pagamentos/adicionar_cartao.html", {
            "request": request,
            "id_fornecedor": id_fornecedor,
            "mensagem": f"Erro ao processar cartão: {str(e)}"
        })


# Mostrar formulário para editar cartão
@router.get("/cartoes/editar/{id_cartao}")
async def mostrar_editar_cartao(request: Request, id_cartao: int, id_fornecedor: int = 1):
    cartao = cartao_repo.obter_cartao_por_id(id_cartao)
    if not cartao or cartao.id_fornecedor != id_fornecedor:
        return RedirectResponse(url="/fornecedor/planos/cartoes", status_code=303)
    
    return templates.TemplateResponse("fornecedor/planos e pagamentos/adicionar_cartao.html", {
        "request": request,
        "cartao": cartao,
        "id_fornecedor": id_fornecedor
    })


# Processar edição de cartão
@router.post("/cartoes/editar/{id_cartao}")
async def editar_cartao(
    request: Request,
    id_cartao: int,
    id_fornecedor: int = Form(...),
    nome_titular: str = Form(...),
    apelido: str = Form(...),
    principal: str = Form(None)
):
    try:
        cartao = cartao_repo.obter_cartao_por_id(id_cartao)
        if not cartao or cartao.id_fornecedor != id_fornecedor:
            return RedirectResponse(url="/fornecedor/planos/cartoes", status_code=303)
        
        # Atualizar dados editáveis
        cartao.nome_titular = nome_titular.strip().upper()
        cartao.apelido = apelido.strip()
        cartao.principal = (principal == "true")
        
        # Salvar alterações
        resultado = cartao_repo.atualizar_cartao(cartao)
        
        if resultado:
            return RedirectResponse(url="/fornecedor/planos/cartoes", status_code=303)
        else:
            return templates.TemplateResponse("fornecedor/planos e pagamentos/adicionar_cartao.html", {
                "request": request,
                "cartao": cartao,
                "id_fornecedor": id_fornecedor,
                "mensagem": "Erro ao atualizar o cartão. Tente novamente."
            })
            
    except Exception as e:
        return templates.TemplateResponse("fornecedor/planos e pagamentos/adicionar_cartao.html", {
            "request": request,
            "cartao": cartao if 'cartao' in locals() else None,
            "id_fornecedor": id_fornecedor,
            "mensagem": f"Erro ao processar alterações: {str(e)}"
        })


# Mostrar confirmação de exclusão
@router.get("/cartoes/excluir/{id_cartao}")
async def mostrar_confirmar_exclusao(request: Request, id_cartao: int, id_fornecedor: int = 1):
    cartao = cartao_repo.obter_cartao_por_id(id_cartao)
    if not cartao or cartao.id_fornecedor != id_fornecedor:
        return RedirectResponse(url="/fornecedor/planos/cartoes", status_code=303)
    
    return templates.TemplateResponse("fornecedor/planos e pagamentos/confirmar_exclusao_cartao.html", {
        "request": request,
        "cartao": cartao
    })


# Processar exclusão de cartão
@router.post("/cartoes/excluir/{id_cartao}")
async def excluir_cartao(request: Request, id_cartao: int, id_fornecedor: int = 1):
    try:
        cartao = cartao_repo.obter_cartao_por_id(id_cartao)
        if not cartao or cartao.id_fornecedor != id_fornecedor:
            return RedirectResponse(url="/fornecedor/planos/cartoes", status_code=303)
        
        # Remover cartão
        resultado = cartao_repo.remover_cartao(id_cartao)
        
        if resultado:
            return RedirectResponse(url="/fornecedor/planos/cartoes", status_code=303)
        else:
            return templates.TemplateResponse("fornecedor/planos e pagamentos/confirmar_exclusao_cartao.html", {
                "request": request,
                "cartao": cartao,
                "mensagem": "Erro ao excluir o cartão. Tente novamente."
            })
            
    except Exception as e:
        return templates.TemplateResponse("fornecedor/planos e pagamentos/confirmar_exclusao_cartao.html", {
            "request": request,
            "cartao": cartao if 'cartao' in locals() else None,
            "mensagem": f"Erro ao processar exclusão: {str(e)}"
        })
