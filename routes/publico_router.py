from fastapi import APIRouter, Request, Query, HTTPException
from fastapi.responses import HTMLResponse
from typing import Optional, List

# Importa a instância de templates do nosso arquivo de configuração
from config import templates

# --- Bloco de Simulação de Dados (sem alterações) ---
class Prestador:
    def __init__(self, id: int, nome: str, area_atuacao: str, avaliacao: float, localizacao: str, logo_url: str, servicos: List[str]):
        self.id, self.nome, self.area_atuacao, self.avaliacao, self.localizacao, self.logo_url, self.servicos = id, nome, area_atuacao, avaliacao, localizacao, logo_url, servicos

class PrestadorRepo:
    def __init__(self):
        self._prestadores: List[Prestador] = [
            Prestador(1, "João Silva Construções", "Construção e Reforma", 4.8, "São Paulo, SP", logo_url="/static/img/logos/construção1.jpg", servicos=["Alvenaria", "Pintura", "Elétrica"]),
            Prestador(2, "Maria Souza Eletricista", "Elétrica", 5.0, "Rio de Janeiro, RJ", logo_url="/static/img/logos/eletricista.jpg", servicos=["Instalação Elétrica", "Reparos"]),
            Prestador(3, "Hidráulica Rápida Ltda", "Hidráulica", 4.5, "Belo Horizonte, MG", logo_url="/static/img/logos/hidráulica.png", servicos=["Encanamento", "Caça Vazamento"]),
            Prestador(4, "Pedro Pinturas", "Pintura e Acabamento", 4.7, "São Paulo, SP", logo_url="/static/img/logos/pintura.webp", servicos=["Pintura Interna", "Pintura Externa", "Textura"]),
            Prestador(5, "Ana Arquiteta", "Arquitetura", 4.9, "Curitiba, PR", logo_url="/static/img/logos/arquitetura.jpeg", servicos=["Projetos Arquitetônicos", "Consultoria"]),
        ]
    def obter_todos(self) -> List[Prestador]: return self._prestadores
    def buscar(self, nome: Optional[str] = None, servico: Optional[str] = None, local: Optional[str] = None) -> List[Prestador]:
        resultado = self._prestadores
        if nome: resultado = [p for p in resultado if nome.lower() in p.nome.lower()]
        if servico: resultado = [p for p in resultado if any(servico.lower() in s.lower() for s in p.servicos)]
        if local: resultado = [p for p in resultado if local.lower() in p.localizacao.lower()]
        return resultado
    def obter_por_id(self, id_prestador: int) -> Optional[Prestador]:
        for p in self._prestadores:
            if p.id == id_prestador: return p
        return None

prestador_repo = PrestadorRepo()
# --- Fim do Bloco de Simulação ---

router = APIRouter(tags=["Público"])

# ==================================================================
# CORREÇÃO DE ORDEM APLICADA AQUI
# ==================================================================

# ROTA 1: A rota específica "/catalogo" vem PRIMEIRO.
@router.get("/catalogo", response_class=HTMLResponse, name="catalogo_prestadores")
async def catalogo_prestadores(
    request: Request,
    q: Optional[str] = Query(None, description="Busca por nome"),
    servico: Optional[str] = Query(None, description="Filtro por serviço"),
    local: Optional[str] = Query(None, description="Filtro por localização")
):
    prestadores_filtrados = prestador_repo.buscar(nome=q, servico=servico, local=local)
    todos_servicos = sorted(list(set(s for p in prestador_repo.obter_todos() for s in p.servicos)))
    return templates.TemplateResponse("publico/catalogo.html", {
        "request": request,
        "prestadores": prestadores_filtrados,
        "servicos_disponiveis": todos_servicos,
        "filtros_ativos": {"q": q, "servico": servico, "local": local}
    })

# ROTA 2: A rota genérica "/prestador/{id_prestador}" vem DEPOIS.
@router.get("/perfil/{id_prestador}", response_class=HTMLResponse, name="detalhes_prestador")
async def detalhes_prestador(request: Request, id_prestador: int):
    prestador = prestador_repo.obter_por_id(id_prestador)
    if not prestador:
        raise HTTPException(status_code=404, detail="Prestador não encontrado")
    return templates.TemplateResponse("publico/perfil_prestador.html", {
        "request": request,
        "prestador": prestador
    })
