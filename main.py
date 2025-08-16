from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Importações dos repositórios (apenas os que precisam criar tabelas no lifespan)
from data.produto import produto_repo
from data.servico import servico_repo

# Importações dos roteadores de fornecedor
from routes.fornecedor.fornecedor_produtos import router as fornecedor_produtos_router
from routes.fornecedor.fornecedor_planos import router as fornecedor_planos_router

# Importações dos roteadores de prestador
from routes.prestador.servicos_oferecidos import router as prestador_servicos_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código que roda na inicialização da aplicação
    print("Iniciando aplicação e criando tabelas no banco de dados...")
    produto_repo.criar_tabela_produto()
    servico_repo.criar_tabela_servico()
    # Adicione aqui a criação de todas as outras tabelas que você tiver
    yield
    # Código que roda no desligamento da aplicação (opcional)
    print("Aplicação desligada.")


app = FastAPI(
    title="Minha Aplicação de Serviços e Produtos",
    description="API para gerenciamento de produtos de fornecedores e serviços de prestadores.",
    version="1.0.0",
    lifespan=lifespan
)

# Configuração de arquivos estáticos e templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Rota principal para teste
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# --- Rotas de Fornecedor ---
app.include_router(fornecedor_produtos_router)
app.include_router(fornecedor_planos_router)

@app.get("/fornecedor", include_in_schema=False)
async def fornecedor_redirect():
    return RedirectResponse(url="/fornecedor/produtos/listar")

# --- Rotas de Prestador ---
app.include_router(prestador_servicos_router)

@app.get("/prestador", include_in_schema=False)
async def prestador_redirect():
    return RedirectResponse(url="/prestador/servicos/listar")

# --- Bloco principal para rodar sem reload ---
if __name__ == "__main__":
    # Rodando sem reload para evitar warnings
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
