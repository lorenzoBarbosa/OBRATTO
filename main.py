from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI(
    title="Obratto",
    description="Plataforma para gerenciamento de produtos de fornecedores e serviços de prestadores.",
    version="1.0.0",
    # lifespan=lifespan
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="sua_chave_secreta")


#PÚBLICO

from routes.publico.publico_routes import router as publico_router # corrigido para refletir a estrutura correta


app.include_router(publico_router)

#FORNECEDOR

from routes.fornecedor.fornecedor_produtos import router as fornecedor_produtos_router
from routes.fornecedor.fornecedor_planos import router as fornecedor_planos_router
from routes.fornecedor import fornecedor_perfil
from routes.fornecedor import fornecedor_promocoes
from routes.fornecedor import fornecedor_solicitacoes



app.include_router(fornecedor_promocoes.router)
app.include_router(fornecedor_perfil.router)
app.include_router(fornecedor_solicitacoes.router)
app.include_router(fornecedor_produtos_router)
app.include_router(fornecedor_planos_router)


#ADMINISTRADOR

from routes.administrador import administrador_anuncios
from routes.administrador import administrador_usuarios


app.include_router(administrador_usuarios.router)
app.include_router(administrador_anuncios.router)



#PRESTADOR

from routes.prestador.prestador_router import router as prestador_router


app.include_router(prestador_router, prefix="/prestador")



#CLIENTE

from routes.cliente.cliente_router import router as cliente_router


app.include_router(cliente_router, prefix="/cliente")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
