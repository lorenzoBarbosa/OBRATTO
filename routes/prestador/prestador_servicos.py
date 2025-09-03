from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates
from data.servico.servico_repo import inserir_servico
from data.servico.servico_model import Servico


router = APIRouter()

# Rota para listar serviços do Prestador 
@router.get("/servicos")
async def listar_servicos(request: Request, q: Optional[str] = None):
    return templates.TemplateResponse("prestador/servicos_listar.html", {"request": request})

# Rota para cadastrar novo serviço
@router.get("/servicos/novo")
async def form_novo_servico(request: Request):
    return templates.TemplateResponse("prestador/servico_form.html", {"request": request})


# Rota POST para cadastrar novo serviço
@router.post("/servicos/novo")
async def cadastrar_servico(
    request: Request,
    nome: str = Form(...),
    descricao: str = Form(...),
    preco: float = Form(...),
):
    try:
        # Cria o dicionário/objeto de serviço
        novo_servico = {
            "nome": nome,
            "descricao": descricao,
            "preco": preco,
        }
        servico_repo.inserir(novo_servico)
        return RedirectResponse(
            url="/servicos",
            status_code=status.HTTP_303_SEE_OTHER
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao cadastrar serviço: {str(e)}"
        )
