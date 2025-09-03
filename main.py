from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from routes.publico import publico_routes
from routes.publico import publico_pagamento
from routes.fornecedor import fornecedor_produtos
from routes.fornecedor import fornecedor_planos
from routes.fornecedor import fornecedor_perfil
from routes.fornecedor import fornecedor_promocoes
from routes.fornecedor import fornecedor_solicitacoes_orcamento
from routes.administrador import administrador_anuncios
from routes.administrador import administrador_usuarios
from routes.prestador import prestador
from routes.prestador import prestador_agenda
from routes.prestador import prestador_planos
from routes.prestador import prestador_solicitacoes
from routes.prestador import prestador_servicos
from routes.cliente import cliente
from routes.cliente import cliente_contratacoes
from routes.cliente import cliente_solicitacao


app = FastAPI(
    title="Obratto",
    description="Plataforma para gerenciamento de produtos de fornecedores e serviços de prestadores.",
    version="1.0.0",
    # lifespan=lifespan
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="sua_chave_secreta")


# PÚBLICO
app.include_router(publico_routes.router)
app.include_router(publico_pagamento.router, prefix="/publico/pagamento")

# FORNECEDOR
app.include_router(fornecedor_promocoes.router, prefix="/fornecedor/promocao")
app.include_router(fornecedor_perfil.router, prefix="/fornecedor")
app.include_router(fornecedor_solicitacoes_orcamento.router, prefix="/fornecedor")
app.include_router(fornecedor_produtos.router, prefix="/fornecedor/produtos")
app.include_router(fornecedor_planos.router, prefix="/fornecedor/planos")

# ADMINISTRADOR
app.include_router(administrador_usuarios.router, prefix="/administrador")
app.include_router(administrador_anuncios.router, prefix="/administrador")

# PRESTADOR
app.include_router(prestador.router, prefix="/prestador")
app.include_router(prestador_agenda.router, prefix="/prestador")
app.include_router(prestador_planos.router, prefix="/prestador")
app.include_router(prestador_solicitacoes.router, prefix="/prestador")   
app.include_router(prestador_servicos.router, prefix="/prestador")


# CLIENTE
app.include_router(cliente.router, prefix="/cliente")
app.include_router(cliente_contratacoes.router, prefix="/cliente")
app.include_router(cliente_solicitacao.router, prefix="/cliente")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
