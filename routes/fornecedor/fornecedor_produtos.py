from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from data.produto.produto_model import Produto
from data.produto import produto_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# Rota home do fornecedor
@router.get("/fornecedor")
async def home_adm(request: Request):
    produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
    return templates.TemplateResponse("fornecedor/home_teste.html", {"request": request, "produtos": produtos})

    
@router.get("/fornecedor/produtos/buscar")
async def buscar_produto(request: Request, id: int = None, nome: str = None):
    produtos = []
    if id is not None:
        produto = produto_repo.obter_produto_por_id(id)
        if produto:
            produtos = [produto]
    elif nome:
        produtos = produto_repo.obter_produto_por_nome(nome)
    return templates.TemplateResponse("fornecedor/produtos/produtos.html", {"request": request, "produtos": produtos})

@router.get("/fornecedor/produtos/listar")
async def listar_produtos(request: Request):
    produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
    response = templates.TemplateResponse("fornecedor/produtos/produtos.html", {"request": request, "produtos": produtos})
    return response

@router.get("/fornecedor/produtos/inserir")
async def mostrar_formulario_produto(request: Request):
    response = templates.TemplateResponse("fornecedor/produtos/cadastrar_produtos.html", {"request": request})
    return response

@router.post("/fornecedor/produtos/inserir")
async def cadastrar_produto(request: Request, nome: str = Form(...), descricao: str = Form(...), preco: float = Form(...), quantidade: int = Form(...)):
    produto = Produto(id=None, nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
    produto_repo.inserir_produto(produto)
    produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
    response = templates.TemplateResponse("fornecedor/produtos/produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto inserido com sucesso"})
    return response

@router.get("/fornecedor/produtos/atualizar/{id}")
async def mostrar_formulario_atualizar_produto(request: Request, id: int):
    produto = produto_repo.obter_produto_por_id(id)
    if produto:
        response = templates.TemplateResponse("fornecedor/produtos/alterar_produtos.html", {"request": request, "produto": produto})
    else:
        produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
        response = templates.TemplateResponse("fornecedor/produtos/produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto não encontrado"})
    return response

@router.post("/fornecedor/produtos/atualizar/{id}")
async def atualizar_produto(request: Request, id: int, nome: str = Form(...), descricao: str = Form(...), preco: float = Form(...), quantidade: int = Form(...)):
    produto = Produto(id=id, nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
    produto_repo.atualizar_produto(produto)
    produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
    response = templates.TemplateResponse("fornecedor/produtos/produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto atualizado com sucesso"})
    return response

@router.post("/fornecedor/produtos/excluir/{id}")
async def excluir_produto(request: Request, id: int):
    produto = produto_repo.obter_produto_por_id(id)
    if produto:
        produto_repo.deletar_produto(id)
        produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
        response = templates.TemplateResponse("fornecedor/produtos/produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto excluído com sucesso"})
    else:
        produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
        response = templates.TemplateResponse("fornecedor/produtos/produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto não encontrado"})
    return response


@router.get("/fornecedor/produtos/excluir/{id}")
async def excluir_produto_get(request: Request, id: int):
    produto = produto_repo.obter_produto_por_id(id)
    if produto:
        produto_repo.deletar_produto(id)
        produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
        response = templates.TemplateResponse("fornecedor/produtos/produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto excluído com sucesso"})
    else:
        produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
        response = templates.TemplateResponse("fornecedor/produtos/produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto não encontrado"})
    return response


@router.get("/fornecedor/produtos/confi_exclusao/{id}")
async def confi_exclusao_produto(request: Request, id: int):
    produto = produto_repo.obter_produto_por_id(id)
    return templates.TemplateResponse("fornecedor/produtos/excluir_produtos.html", {"request": request, "produto": produto})
