from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates
router = APIRouter()


# Tudo funcionando perfeitamente

# Rota para listar serviços do Prestador 
@router.get("/meus/servicos")
async def listar_servicos(request: Request):
    return templates.TemplateResponse("prestador/servicos/meus_servicos.html", {"request": request})


# Rota para cadastrar novo serviço
@router.get("/novo")
async def form_novo_servicos(request: Request):
    return templates.TemplateResponse("prestador/servicos/novo.html", {"request": request})

# Editar serviço
@router.get("/editar/servicos")
async def editar_servicos(request: Request, id_servico: int):
    return templates.TemplateResponse("prestador/servicos/editar_servico.html", {"request": request, "id_servico": id_servico})

# Detalhes do serviço
@router.get("/detalhes")
async def detalhes_servicos(request: Request, id_servico: int):
    return templates.TemplateResponse("prestador/servicos/detalhes.html", {"request": request, "id_servico": id_servico})

# Buscar serviço
@router.get("/buscar")
async def buscar_servicos(request: Request, id_servico: int):
    return templates.TemplateResponse("prestador/servicos/buscar.html", {"request": request, "id_servico": id_servico})

# status do serviço
@router.get("/status")
async def status_servicos(request: Request, id_servico: int): 
    return templates.TemplateResponse("prestador/servicos/status.html", {"request": request, "id_servico": id_servico})

# Excluir serviço
@router.get("/servicos/excluir")
async def excluir_servico(request: Request, id_servico: int):
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
