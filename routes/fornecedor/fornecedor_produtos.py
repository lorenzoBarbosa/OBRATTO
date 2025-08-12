from fastapi import APIRouter, form, Request
from fastapi.templating import Jinja2Templates

from data.produto.produto_model import Produto
from data.produto import produto_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/fornecedor/produtos/listar")
async def listar_produtos(request: Request):
    produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
    response = templates.TemplateResponse("listar_produtos.html", {"request": request, "produtos": produtos})
    return response

# router.post("/fornecedor/produtos/listar")
# async def listar_produtos_post(request: Request, page: int = form.Field(...)):
#     produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=(page - 1) * 10)
#     response = templates.TemplateResponse("listar_produtos.html", {"request": request, "produtos": produtos})
#     return response

router.get("/fornecedor/produtos/inserir")
async def cadastrar_produto(request: Request):
    produtos = produto_repo.inserir_produto(Produto(id=1, nome="Produto Exemplo", descricao="Descrição do produto", preco=10.0, quantidade=100))
    if produtos:
        response = templates.TemplateResponse("listar_produtos.html", {"request": request, "produtos": produtos})
    else:
        response = templates.TemplateResponse("inserir_produto.html", {"request": request})
    return response


@router.get("/fornecedor/produtos/atualizar/{id}")
async def atualizar_produto(request: Request, id: int):
    produto = produto_repo.obter_produto_por_id(id)
    if produto:
        response = templates.TemplateResponse("atualizar_produto.html", {"request": request, "produto": produto})
    else:
        response = templates.TemplateResponse("listar_produtos.html", {"request": {}, "mensagem": "Produto não encontrado"})
    return response

# @router.post("/fornecedor/produtos/atualizar/{id}")
# async def atualizar_produto_post(request: Request, id: int, nome: str = form.Field(...), descricao: str = form.Field(...), preco: float = form.Field(...), quantidade: int = form.Field(...)):
#     produto = Produto(id=id, nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
#     produto_repo.atualizar_produto(produto)
#     produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
#     response = templates.TemplateResponse("listar_produtos.html", {"request": request, "produtos": produtos})
#     return response

@router.get("/fornecedor/produtos/excluir/{id}")
async def excluir_produto(request: Request, id: int):
    produto = produto_repo.obter_produto_por_id(id)
    if produto:
        produto_repo.deletar_produto(id)
        response = templates.TemplateResponse("listar_produtos.html", {"request": request, "mensagem": "Produto excluído com sucesso"})
    else:
        response = templates.TemplateResponse("listar_produtos.html", {"request": {}, "mensagem": "Produto não encontrado"})
    return response

