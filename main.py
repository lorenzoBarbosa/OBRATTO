from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from data.produto import produto_repo
from data.administrador import administrador_repo
from data.fornecedor import fornecedor_repo
from data.cliente import cliente_repo
from data.prestador import prestador_repo
from data.plano import plano_repo
from data.anuncio import anuncio_repo
from data.avaliacao import avaliacao_repo
from data.mensagem import mensagem_repo
from data.notificacao import notificacao_repo
from data.orcamento import orcamento_repo
from data.orcamentoservico import orcamento_servico_repo
from data.servico import servico_repo
from data.usuario import usuario_repo

#fornecedor

from routes.fornecedor.fornecedor_produtos import router as fornecedor_produtos_router

#administrador

from routes.administrador.administrador_routes import router as administrador_router

#cliente

#prestador



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

#criar as tabelas chamando a função repo.

produto_repo.criar_tabela_produto()

# Rota principal para teste
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#rotas

app.include_router(fornecedor_produtos_router)
app.include_router(administrador_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)


