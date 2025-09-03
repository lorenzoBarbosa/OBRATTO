from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates
router = APIRouter()

# Rota para listar serviços do Prestador 
@router.get("/meus/servicos")
async def listar_servicos(request: Request):
    return templates.TemplateResponse("prestador/servicos_listar.html", {"request": request})


# Rota para cadastrar novo serviço
@router.get("/servicos/novo")
async def form_novo_servico(request: Request):
    return templates.TemplateResponse("prestador/servico_form.html", {"request": request})

# Editar serviço
@router.get("/servicos/editar")
async def editar_servico(request: Request, id_servico: int):
    return templates.TemplateResponse("prestador/servico_editar.html", {"request": request, "id_servico": id_servico})

# Excluir serviço
@router.get("/servicos/excluir")
async def excluir_servico(request: Request, id_servico: int):
    return templates.TemplateResponse("prestador/servico_excluir.html", {"request": request, "id_servico": id_servico})























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
