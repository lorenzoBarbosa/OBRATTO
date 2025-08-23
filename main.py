from fastapi import FastAPI, Request, HTTPException
from contextlib import asynccontextmanager
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

# --- Importações Centralizadas e dos Roteadores ---
from config import templates
from routes.cliente.cliente_router import router as cliente_router
from routes.fornecedor.fornecedor_produtos import router as fornecedor_produtos_router
from routes.fornecedor.fornecedor_planos import router as fornecedor_planos_router
from routes.prestador.prestador_router import router as prestador_router
from routes.publico_router import router as publico_router 
from routes.cadastro.cadastro_router import router as cadastro_router

# --- Bloco de Simulação para Repositórios ---
try:
    from data.produto import produto_repo
    from data.servico import servico_repo
except ImportError:
    class DummyRepo:
        def criar_tabela_produto(self): pass
        def criar_tabela_servico(self): pass
    produto_repo = DummyRepo()
    servico_repo = DummyRepo()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando aplicação e criando tabelas no banco de dados...")
    produto_repo.criar_tabela_produto()
    servico_repo.criar_tabela_servico()
    yield
    print("Aplicação desligada.")

app = FastAPI(
    title="Obratto",
    description="Plataforma para gerenciamento de produtos de fornecedores e serviços de prestadores.",
    version="1.0.0",
    lifespan=lifespan
)

# Configuração de arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- Rota Principal (CORRIGIDA) ---
@app.get("/", response_class=RedirectResponse, include_in_schema=False)
async def read_root(request: Request):
    try:
        # --- A ÚNICA MUDANÇA ESTÁ AQUI ---
        # Trocamos 'painel_prestador' por 'catalogo_prestadores' para que a página
        # inicial do site seja o catálogo público.
        return RedirectResponse(url=request.url_for('catalogo_prestadores'))
    except Exception as e:
        print(f"ERRO CRÍTICO ao gerar URL para 'catalogo_prestadores': {e}")
        raise HTTPException(status_code=500, detail="Erro na configuração da rota principal.")

# --- Inclusão dos Roteadores ---
app.include_router(publico_router)
app.include_router(prestador_router)
app.include_router(fornecedor_produtos_router)
app.include_router(fornecedor_planos_router)
app.include_router(cliente_router)
app.include_router(cadastro_router)


@app.get("/fornecedor", include_in_schema=False, response_class=RedirectResponse)
async def fornecedor_redirect():
    return RedirectResponse(url="/fornecedor/produtos/listar")

# --- Bloco de Execução ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
