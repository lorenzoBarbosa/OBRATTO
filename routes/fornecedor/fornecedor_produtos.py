from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from data.produto.produto_model import Produto
from data.produto import produto_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Rota home do fornecedor
@router.get("/fornecedor")
async def home_fornecedor(request: Request):
    response = templates.TemplateResponse("fornecedor/home_fornecedor.html", {"request": request})
    return response

# Rota de debug para verificar se o banco está funcionando
@router.get("/fornecedor/produtos/debug")
async def debug_produtos(request: Request):
    try:
        from utils.db import get_database_info
        
        # Informações do banco
        db_info = get_database_info()
        
        # Tenta criar a tabela
        produto_repo.criar_tabela_produto()
        
        # Tenta buscar produtos
        produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
        
        debug_info = {
            "database_info": db_info,
            "tabela_criada": True,
            "total_produtos": len(produtos),
            "produtos": [
                {
                    "id": p.id,
                    "nome": p.nome,
                    "descricao": p.descricao,
                    "preco": p.preco,
                    "quantidade": p.quantidade
                } for p in produtos
            ]
        }
        
        return {"debug": debug_info, "status": "ok"}
    except Exception as e:
        return {"error": str(e), "status": "error"}

@router.get("/fornecedor/produtos/listar")
async def listar_produtos(request: Request):
    produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
    response = templates.TemplateResponse("fornecedor/listar_produtos.html", {"request": request, "produtos": produtos})
    return response

@router.get("/fornecedor/produtos/inserir")
async def mostrar_formulario_produto(request: Request):
    response = templates.TemplateResponse("fornecedor/inserir_produtos.html", {"request": request})
    return response

@router.post("/fornecedor/produtos/inserir")
async def cadastrar_produto(request: Request, nome: str = Form(...), descricao: str = Form(...), preco: float = Form(...), quantidade: int = Form(...)):
    produto = Produto(id=None, nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
    produto_repo.inserir_produto(produto)
    produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
    response = templates.TemplateResponse("fornecedor/listar_produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto inserido com sucesso"})
    return response

@router.get("/fornecedor/produtos/atualizar/{id}")
async def mostrar_formulario_atualizar_produto(request: Request, id: int):
    produto = produto_repo.obter_produto_por_id(id)
    if produto:
        response = templates.TemplateResponse("fornecedor/atualizar_produtos.html", {"request": request, "produto": produto})
    else:
        produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
        response = templates.TemplateResponse("fornecedor/listar_produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto não encontrado"})
    return response

@router.post("/fornecedor/produtos/atualizar/{id}")
async def atualizar_produto(request: Request, id: int, nome: str = Form(...), descricao: str = Form(...), preco: float = Form(...), quantidade: int = Form(...)):
    produto = Produto(id=id, nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
    produto_repo.atualizar_produto(produto)
    produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
    response = templates.TemplateResponse("fornecedor/listar_produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto atualizado com sucesso"})
    return response

@router.post("/fornecedor/produtos/excluir/{id}")
async def excluir_produto(request: Request, id: int):
    produto = produto_repo.obter_produto_por_id(id)
    if produto:
        produto_repo.deletar_produto(id)
        produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
        response = templates.TemplateResponse("fornecedor/listar_produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto excluído com sucesso"})
    else:
        produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
        response = templates.TemplateResponse("fornecedor/listar_produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto não encontrado"})
    return response

# Rota GET para excluir (backup/compatibilidade)
@router.get("/fornecedor/produtos/excluir/{id}")
async def excluir_produto_get(request: Request, id: int):
    produto = produto_repo.obter_produto_por_id(id)
    if produto:
        produto_repo.deletar_produto(id)
        produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
        response = templates.TemplateResponse("fornecedor/listar_produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto excluído com sucesso"})
    else:
        produtos = produto_repo.obter_produto_por_pagina(limit=10, offset=0)
        response = templates.TemplateResponse("fornecedor/listar_produtos.html", {"request": request, "produtos": produtos, "mensagem": "Produto não encontrado"})
    return response
