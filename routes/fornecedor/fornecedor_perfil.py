from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from data.fornecedor.fornecedor_model import Fornecedor
from data.fornecedor import fornecedor_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cadastro")
async def exibir_cadastro_fornecedor(request: Request):
    return templates.TemplateResponse("fornecedor/cadastro_fornecedor.html", {"request": request})

# Visualizar perfil do fornecedor
@router.get("/conta/{id}")
async def visualizar_conta(request: Request, id: int):
    fornecedor = fornecedor_repo.obter_fornecedor_por_id(id)
    return templates.TemplateResponse("fornecedor/conta.html", {"request": request, "fornecedor": fornecedor})

# Excluir conta do fornecedor
@router.post("/conta/excluir/{id}")
async def excluir_conta(request: Request, id: int):
    fornecedor = fornecedor_repo.obter_fornecedor_por_id(id)
    if fornecedor:
        fornecedor_repo.deletar_fornecedor(id)
        mensagem = "Conta excluída com sucesso"
        fornecedor = None
    else:
        mensagem = "Fornecedor não encontrado"
    return templates.TemplateResponse("fornecedor/conta.html", {"request": request, "fornecedor": fornecedor, "mensagem": mensagem})

@router.get("/perfil_publico/{id}")
async def exibir_perfil_publico(request: Request, id: int):
    fornecedor = fornecedor_repo.obter_fornecedor_por_id(id)
    return templates.TemplateResponse("fornecedor/perfil.html", {"request": request, "fornecedor": fornecedor})


