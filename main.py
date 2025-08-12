from fastapi import FastAPI
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


app.include_router(fornecedor_produtos_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)


'''from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from utils.db import open_connection

from data.usuario.usuario_sql import CRIAR_TABELA_USUARIO
from data.cliente.cliente_sql import CRIAR_TABELA_CLIENTE
from data.fornecedor.fornecedor_sql import CRIAR_TABELA_FORNECEDOR
from data.prestador.prestador_sql import CRIAR_TABELA_PRESTADOR
from data.administrador.administrador_sql import CRIAR_TABELA_ADMINISTRADOR
from data.notificacao.notificacao_sql import CRIAR_TABELA_NOTIFICACAO
from data.mensagem.mensagem_sql import CRIAR_TABELA_MENSAGEM
from data.plano.plano_sql import CRIAR_TABELA_PLANO
from data.orcamento.orcamento_sql import CRIAR_TABELA_ORCAMENTO
from data.orcamentoservico.orcamento_servico_sql import CRIAR_TABELA_ORCAMENTO_SERVICO
from data.servico.servico_sql import CRIAR_TABELA_SERVICO
from data.anuncio.anuncio_sql import CRIAR_TABELA_ANUNCIO
from data.avaliacao.avaliacao_sql import CRIAR_TABELA_AVALIACAO
from data.inscricaoplano.inscricao_plano_sql import CRIAR_TABELA_INSCRICAO_PLANO


def criar_tabela(sql_criar_tabela: str) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql_criar_tabela)
        conn.commit()
        return True


def main():
    tabelas = [
        CRIAR_TABELA_USUARIO,
        CRIAR_TABELA_CLIENTE,
        CRIAR_TABELA_FORNECEDOR,
        CRIAR_TABELA_PRESTADOR,
        CRIAR_TABELA_ADMINISTRADOR,
        CRIAR_TABELA_NOTIFICACAO,
        CRIAR_TABELA_MENSAGEM,
        CRIAR_TABELA_PLANO,
        CRIAR_TABELA_ORCAMENTO,
        CRIAR_TABELA_ORCAMENTO_SERVICO,
        CRIAR_TABELA_SERVICO,
        CRIAR_TABELA_ANUNCIO,
        CRIAR_TABELA_AVALIACAO,
        CRIAR_TABELA_INSCRICAO_PLANO,
    ]

    for i, tabela_sql in enumerate(tabelas, start=1):
        sucesso = criar_tabela(tabela_sql)
        print(f"Tabela {i} criada com sucesso? {sucesso}")



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get_root():
    response = templates.TemplateResponse("base.html", {"request": {}})
    return response

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
'''