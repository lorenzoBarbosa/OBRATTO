from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from data.cliente import cliente_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/{id}")
async def get_cliente(request: Request, id: int):
    cliente = cliente_repo.obter_cliente_por_id(id)
    return templates.TemplateResponse("cliente.html", {"request": request, "cliente": cliente})# Salve como: routes/cliente_router.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from typing import List
from datetime import datetime, timedelta
from config import templates

# --- Bloco de Simulação de Dados ---

class Contratacao:
    def __init__(self, id: int, prestador_nome: str, servico: str, data_inicio: datetime, status: str, valor: float):
        self.id = id
        self.prestador_nome = prestador_nome
        self.servico = servico
        self.data_inicio = data_inicio
        self.status = status # "Em andamento", "Concluído", "Cancelado"
        self.valor = valor

class Solicitacao:
    def __init__(self, id: int, prestador_nome: str, servico: str, data_solicitacao: datetime, status: str):
        self.id = id
        self.prestador_nome = prestador_nome
        self.servico = servico
        self.data_solicitacao = data_solicitacao
        self.status = status # "Aguardando resposta", "Aceito", "Recusado"

class ClienteRepo:
    def __init__(self):
        # Dados de exemplo
        self._contratacoes: List[Contratacao] = [
            Contratacao(1, "João Silva Construções", "Construção de Parede", datetime.now() - timedelta(days=10), "Em andamento", 1500.00),
            Contratacao(2, "Pedro Pinturas", "Pintura Interna", datetime.now() - timedelta(days=30), "Concluído", 850.00),
        ]
        self._solicitacoes: List[Solicitacao] = [
            Solicitacao(1, "Maria Souza Eletricista", "Instalação Elétrica", datetime.now() - timedelta(days=2), "Aguardando resposta"),
            Solicitacao(2, "Hidráulica Rápida Ltda", "Caça Vazamento", datetime.now() - timedelta(days=5), "Aceito"),
        ]

    def obter_contratacoes(self, id_cliente: int) -> List[Contratacao]:
        # Em um app real, você filtraria por id_cliente
        return self._contratacoes

    def obter_solicitacoes(self, id_cliente: int) -> List[Solicitacao]:
        # Em um app real, você filtraria por id_cliente
        return self._solicitacoes

cliente_repo = ClienteRepo()
# --- Fim do Bloco de Simulação ---

router = APIRouter(prefix="/cliente", tags=["Cliente"])

# ROTA 1: Home do Cliente (Dashboard)
@router.get("/", response_class=HTMLResponse, name="home_cliente")
async def home_cliente(request: Request):
    id_cliente_logado = 1 # Simulação
    return templates.TemplateResponse("cliente/home.html", {
        "request": request,
        "id_cliente": id_cliente_logado,
        "pagina_ativa": "home"
    })

# ROTA 2: Lista de Contratações
@router.get("/contratacoes", response_class=HTMLResponse, name="cliente_contratacoes")
async def cliente_contratacoes(request: Request):
    id_cliente_logado = 1 # Simulação
    contratacoes = cliente_repo.obter_contratacoes(id_cliente_logado)
    return templates.TemplateResponse("cliente/contratacoes.html", {
        "request": request,
        "contratacoes": contratacoes,
        "id_cliente": id_cliente_logado,
        "pagina_ativa": "contratacoes"
    })

# ROTA 3: Lista de Solicitações de Contratação
@router.get("/solicitacoes", response_class=HTMLResponse, name="cliente_solicitacoes")
async def cliente_solicitacoes(request: Request):
    id_cliente_logado = 1 # Simulação
    solicitacoes = cliente_repo.obter_solicitacoes(id_cliente_logado)
    return templates.TemplateResponse("cliente/solicitacoes.html", {
        "request": request,
        "solicitacoes": solicitacoes,
        "id_cliente": id_cliente_logado,
        "pagina_ativa": "solicitacoes"
    })
