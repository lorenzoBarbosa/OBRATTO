from fastapi import APIRouter, Request, Form, status
from fastapi.responses import RedirectResponse
from config import templates

router = APIRouter()


#Meu plano
@router.get("/meu/plano")
async def meu_plano(request: Request):
    return templates.TemplateResponse("prestador/planos/meu_plano.html", {"request": request})

#Página principal de planos
@router.get("/planos")
async def planos_prestador(request: Request):
    return templates.TemplateResponse("prestador/planos/planos.html", {"request": request})

#Assinar plano
@router.get("/planos/assinar")
async def assinar_plano(request: Request):
    return templates.TemplateResponse("prestador/planos/assinar.html", {"request": request})

#Editar plano
@router.get("/planos/editar")
async def exibir_formulario_edicao(request: Request, id_prestador: int):
    return templates.TemplateResponse("prestador/planos/editar.html", {"request": request, "id_prestador": id_prestador})

#Renovar plano 
@router.get("/planos/renovar")
async def exibir_pagina_renovacao(request: Request):
    return templates.TemplateResponse("prestador/planos/renovar.html", {"request": request})

#Cancelar plano 
@router.get("/planos/cancelar")
async def exibir_pagina_cancelamento(request: Request, id_prestador: int):
    return templates.TemplateResponse(
        "prestador/planos/cancelar.html",
        {"request": request, "id_prestador": id_prestador}
    )

#Confirmação de cancelamento
@router.get("confirmar/cancelamento")
async def confirmar_cancelamento(request: Request):
    return templates.TemplatesResponse("prestador/confirmar_cancelamento.html", {"request": Request})




# # Rota post para editar plano
# @router.post("/planos/editar", name="processar_edicao_assinatura")
# async def processar_edicao_assinatura(
#     request: Request,
#     id_prestador: int = Form(...),
#     id_plano: int = Form(...)
# ):
#     try:
#         assinatura_ativa = inscricao_plano_repo.obter_inscricao_por_prestador(id_prestador=id_prestador)
#         if not assinatura_ativa:
#             return templates.TemplateResponse("prestador/planos_editar.html", {
#                 "request": request, 
#                 "mensagem": "Você não possui plano ativo para alterar."
#             })
#         plano = plano_repo.obter_plano_por_id(id_plano)
#         if plano:
#             # Atualiza o plano na inscrição ativa
#             assinatura_ativa.id_plano = id_plano
#             sucesso = inscricao_plano_repo.atualizar_inscricao_plano(assinatura_ativa)
#             if sucesso:
#                 return templates.TemplateResponse("prestador/planos_editar.html", {
#                     "request": request, 
#                     "mensagem": f"Plano alterado com sucesso para: {plano.nome_plano}"
#                 })
#             else:
#                 return templates.TemplateResponse("prestador/planos_editar.html", {
#                     "request": request, 
#                     "mensagem": "Erro ao atualizar o plano no banco de dados."
#                 })
#         else:
#             return templates.TemplateResponse("prestador/planos_editar.html", {
#                 "request": request, 
#                 "mensagem": "Plano selecionado não encontrado."
#             })
#     except Exception as e:
#         return templates.TemplateResponse("prestador/planos_editar.html", {
#             "request": request, 
#             "mensagem": f"Erro ao alterar plano: {str(e)}"
#         })




# Rota post para renovar plano
# @router.post("/planos/renovar", name="processar_renovacao_plano")
# async def processar_renovacao_plano(
#     request: Request,
#     id_prestador: int = Form(...)
# ):
#     contexto = {"request": request}
#     try:
#         sucesso_renovacao = inscricao_plano_repo.renovar_assinatura(id_prestador=id_prestador)
#         if sucesso_renovacao:
#             contexto["mensagem"] = "Seu plano foi renovado com sucesso por mais 30 dias!"
#             contexto["sucesso"] = True
#         else:
#             contexto["mensagem"] = "Não foi possível encontrar uma assinatura ativa para renovar."
#             contexto["sucesso"] = False
#     except Exception as e:
#         contexto["mensagem"] = "Ocorreu um erro inesperado ao tentar processar a renovação."
#         contexto["sucesso"] = False
#     return templates.TemplateResponse("prestador/planos_renovar.html", contexto)



# Rota post para cancelar plano
# @router.post("/planos/cancelar", name="processar_cancelamento_plano")
# async def processar_cancelamento_plano(
#     request: Request,
#     id_prestador: int = Form(...),
#     confirmacao: str = Form(...)
# ):
#     try:
#         assinatura_ativa = inscricao_plano_repo.obter_inscricao_por_prestador(id_prestador=id_prestador)
#         if not assinatura_ativa:
#             return templates.TemplateResponse("prestador/planos_cancelar.html", {
#                 "request": request, "mensagem": "Você não possui assinatura ativa para cancelar."
#             })
#         if confirmacao.lower() == "confirmar":
#             sucesso = inscricao_plano_repo.deletar_inscricao_plano(assinatura_ativa.id_inscricao_plano)
#             if sucesso:
#                 return templates.TemplateResponse("prestador/planos_cancelar.html", {
#                     "request": request, "mensagem": "Plano cancelado com sucesso!", "cancelado": True
#                 })
#             else:
#                 return templates.TemplateResponse("prestador/planos_cancelar.html", {
#                     "request": request, "mensagem": "Ocorreu um erro ao tentar cancelar o plano no banco de dados."
#                 })
#         else:
#             return templates.TemplateResponse("prestador/planos_cancelar.html", {
#                 "request": request, "mensagem": "Cancelamento não confirmado. Digite 'confirmar' para prosseguir."
#             })
#     except Exception as e:
#         return templates.TemplateResponse("prestador/planos_cancelar.html", {
#             "request": request, "mensagem": f"Erro inesperado ao processar o cancelamento: {str(e)}"
#         })