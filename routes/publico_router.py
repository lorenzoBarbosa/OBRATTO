from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from typing import Optional, List

# Importa a instância de templates do nosso arquivo de configuração
from config import templates


class Prestador:
    def __init__(self, id: int, nome: str, area_atuacao: str, avaliacao: float, localizacao: str, logo_url: str, servicos: List[str]):
        self.id = id
        self.nome = nome
        self.area_atuacao = area_atuacao
        self.avaliacao = avaliacao
        self.localizacao = localizacao
        self.logo_url = logo_url
        self.servicos = servicos

class PrestadorRepo:
    def __init__(self):
        # --- CORREÇÃO APLICADA AQUI ---
        # A lista _prestadores foi atualizada para usar os nomes de arquivo corretos.
        self._prestadores: List[Prestador] = [
            Prestador(1, "João Silva Construções", "Construção e Reforma", 4.8, "São Paulo, SP", 
                      logo_url="/static/img/logos/construção1.jpg",
                      servicos=["Alvenaria", "Pintura", "Elétrica"]),
            
            Prestador(2, "Maria Souza Eletricista", "Elétrica", 5.0, "Rio de Janeiro, RJ", 
                      logo_url="/static/img/logos/eletricista.jpg",
                      servicos=["Instalação Elétrica", "Reparos"]),
            
            Prestador(3, "Hidráulica Rápida Ltda", "Hidráulica", 4.5, "Belo Horizonte, MG", 
                      logo_url="/static/img/logos/hidráulica.png",
                      servicos=["Encanamento", "Caça Vazamento"]),
            
            Prestador(4, "Pedro Pinturas", "Pintura e Acabamento", 4.7, "São Paulo, SP", 
                      logo_url="/static/img/logos/pintura.webp",
                      servicos=["Pintura Interna", "Pintura Externa", "Textura"]),
            
            Prestador(5, "Ana Arquiteta", "Arquitetura", 4.9, "Curitiba, PR", 
                      logo_url="/static/img/logos/arquitetura.jpeg",
                      servicos=["Projetos Arquitetônicos", "Consultoria"]),
        ]
   

    def obter_todos(self) -> List[Prestador]:
        return self._prestadores

    def buscar(self, nome: Optional[str] = None, servico: Optional[str] = None, local: Optional[str] = None) -> List[Prestador]:
        resultado = self._prestadores
        if nome:
            resultado = [p for p in resultado if nome.lower() in p.nome.lower()]
        if servico:
            resultado = [p for p in resultado if any(servico.lower() in s.lower() for s in p.servicos)]
        if local:
            resultado = [p for p in resultado if local.lower() in p.localizacao.lower()]
        return resultado

prestador_repo = PrestadorRepo()


router = APIRouter(tags=["Público"])

@router.get("/catalogo", response_class=HTMLResponse, name="catalogo_prestadores")
async def catalogo_prestadores(
    request: Request,
    q: Optional[str] = Query(None, description="Busca por nome"),
    servico: Optional[str] = Query(None, description="Filtro por serviço"),
    local: Optional[str] = Query(None, description="Filtro por localização")
):
    # Busca os prestadores com base nos filtros
    prestadores_filtrados = prestador_repo.buscar(nome=q, servico=servico, local=local)
    
    # Simula uma lista de serviços para o dropdown de filtro
    todos_servicos = sorted(list(set(s for p in prestador_repo.obter_todos() for s in p.servicos)))

    return templates.TemplateResponse("publico/catalogo.html", {
        "request": request,
        "prestadores": prestadores_filtrados,
        "servicos_disponiveis": todos_servicos,
        "filtros_ativos": {"q": q, "servico": servico, "local": local}
    })
