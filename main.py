from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles

from routes.publico_routes import router as publico_router # alterado por maroquio

# from routes.administrador import administrador_anuncios
# from routes.cliente.cliente_router import router as cliente_router
# from routes.fornecedor.fornecedor_produtos import router as fornecedor_produtos_router
# from routes.fornecedor.fornecedor_planos import router as fornecedor_planos_router
# from routes.fornecedor import fornecedor_perfil
# from routes.fornecedor import fornecedor_promocoes
# from routes.fornecedor import fornecedor_solicitacoes
# from routes.administrador import administrador_usuarios
# from routes.administrador import administrador_anuncios
# from routes.prestador.prestador_router import router as prestador_router
# from routes.cadastro.cadastro_router import router as cadastro_router


# try:
#     from data.produto import produto_repo
#     from data.servico import servico_repo
# except ImportError:
#     class DummyRepo:
#         def criar_tabela_produto(self): pass
#         def criar_tabela_servico(self): pass
#     produto_repo = DummyRepo()
#     servico_repo = DummyRepo()

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     print("Iniciando aplicação e criando tabelas no banco de dados...")
#     produto_repo.criar_tabela_produto()
#     servico_repo.criar_tabela_servico()
#     yield
#     print("Aplicação desligada.")

app = FastAPI(
    title="Obratto",
    description="Plataforma para gerenciamento de produtos de fornecedores e serviços de prestadores.",
    version="1.0.0",
    # lifespan=lifespan
)
app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(publico_router)
# app.include_router(prestador_router)
# app.include_router(cliente_router)
# app.include_router(cadastro_router)

#fornecedor
# app.include_router(fornecedor_promocoes.router)
# app.include_router(fornecedor_perfil.router)
# app.include_router(fornecedor_solicitacoes.router)
# app.include_router(fornecedor_produtos_router)
# app.include_router(fornecedor_planos_router)

#Adm
# app.include_router(administrador_usuarios.router)
# app.include_router(administrador_anuncios.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
