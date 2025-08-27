from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from routes.publico import publico_routes
from routes.fornecedor import fornecedor_produtos
from routes.fornecedor import fornecedor_planos
from routes.fornecedor import fornecedor_perfil
from routes.fornecedor import fornecedor_promocoes
from routes.fornecedor import fornecedor_solicitacoes_orcamento
from routes.administrador import administrador_anuncios
from routes.administrador import administrador_usuarios
from routes.prestador import prestador
from routes.cliente import cliente



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

# FORNECEDOR
app.include_router(fornecedor_promocoes.router)
app.include_router(fornecedor_perfil.router)
app.include_router(fornecedor_solicitacoes_orcamento.router)
app.include_router(fornecedor_produtos.router)
app.include_router(fornecedor_planos.router)

# ADMINISTRADOR
app.include_router(administrador_usuarios.router)
app.include_router(administrador_anuncios.router)

# PRESTADOR
app.include_router(prestador.router, prefix="/prestador")

# CLIENTE
app.include_router(cliente.router, prefix="/cliente")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
