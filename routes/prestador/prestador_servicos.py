from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates
from utils.auth_decorator import requer_autenticacao
router = APIRouter()


# Tudo funcionando perfeitamente

# Rota para listar serviços do Prestador 
@router.get("/meus/servicos")
async def listar_servicos(request: Request):
    return templates.TemplateResponse("prestador/servicos/meus_servicos.html", {"request": request})


# Rota para cadastrar novo serviço
@router.get("/novo")
@requer_autenticacao(["prestador"])
async def form_novo_servicos(request: Request):
    return templates.TemplateResponse("prestador/servicos/novo.html", {"request": request})

# Rota para processar o formulário de novo serviço
@router.post("/novo")
@requer_autenticacao(["prestador"])
async def processar_novo_servico(request: Request,
    id_servico: int = Form(...), 
    id_prestador: int = Form(...), 
    titulo: str = Form(...),
    descricao: str = Form(...),
    categoria: str = Form(...),
    valor_base: float = Form(...),
    nome_prestador: str = Form(...)):
    return templates.TemplateResponse("prestador/servicos/novo.html", {"request": request})

# Editar serviço
@router.get("/editar/servicos")
@requer_autenticacao(["prestador"])
async def editar_servicos(request: Request, id_servico: int):
    return templates.TemplateResponse("prestador/servicos/editar_servico.html", {"request": request, "id_servico": id_servico})

# Rota para processar o formulário de edição do serviço
@router.post("/editar/servicos")
@requer_autenticacao(["prestador"])
async def processar_edicao_servico(request: Request, 
    id_servico: int = Form(...), 
    id_prestador: int = Form(...), 
    titulo: str = Form(...),
    descricao: str = Form(...),
    categoria: str = Form(...),
    valor_base: float = Form(...),
    nome_prestador: str = Form(...)):
    return templates.TemplateResponse("prestador/servicos/editar_servico.html", {"request": request})

# Detalhes do serviço
@router.get("/detalhes")
@requer_autenticacao(["prestador"])
async def detalhes_servicos(request: Request, id_servico: int):
    return templates.TemplateResponse("prestador/servicos/detalhes.html", {"request": request, "id_servico": id_servico})

# Buscar serviço
@router.get("/buscar")
@requer_autenticacao(["prestador"])
async def buscar_servicos(request: Request, id_servico: int):
    return templates.TemplateResponse("prestador/servicos/buscar.html", {"request": request, "id_servico": id_servico})

# status do serviço
@router.get("/status")
@requer_autenticacao(["prestador"])
async def status_servicos(request: Request, id_servico: int): 
    return templates.TemplateResponse("prestador/servicos/status.html", {"request": request, "id_servico": id_servico})

# Excluir serviço
@router.get("/servicos/excluir")
@requer_autenticacao(["prestador"])
async def excluir_servico(request: Request, id_servico: int):
    return templates.TemplateResponse("prestador/servicos/excluir.html", {"request": request, "id_servico": id_servico})

# Rota para processar a exclusão do serviço
@router.post("/servicos/excluir")
@requer_autenticacao(["prestador"])
async def processar_exclusao_servico(request: Request, 
    id_servico: int = Form(...), 
    id_prestador: int = Form(...), 
    titulo: str = Form(...),
    descricao: str = Form(...),
    categoria: str = Form(...),
    valor_base: float = Form(...),
    nome_prestador: str = Form(...)):
    return templates.TemplateResponse("prestador/servicos/excluir.html", {"request": request, "id_servico": id_servico})





















# # Rota POST para cadastrar novo serviço
# @router.post("/servicos/novo")
# async def cadastrar_servico(
#     request: Request,
#     nome: str = Form(...),
#     descricao: str = Form(...),
#     preco: float = Form(...),
# ):
#     try:
#         # Cria o dicionário/objeto de serviço
#         novo_servico = {
#             "nome": nome,
#             "descricao": descricao,
#             "preco": preco,
#         }
#         servico_repo.inserir(novo_servico)
#         return RedirectResponse(
#             url="/servicos",
#             status_code=status.HTTP_303_SEE_OTHER
#         )
#     except Exception as e:
#         raise HTTPException(
#             status_code=500,
#             detail=f"Erro ao cadastrar serviço: {str(e)}"
#         )
