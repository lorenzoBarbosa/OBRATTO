# Salve como: routes/publico_router.py

from fastapi import APIRouter, Request, Query, HTTPException, Form
from fastapi.responses import HTMLResponse
from typing import Optional, List
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

# ROTA 1: Catálogo
@router.get("/catalogo", response_class=HTMLResponse, name="catalogo_prestadores")
async def catalogo_prestadores(request: Request, q: Optional[str] = Query(None), servico: Optional[str] = Query(None), local: Optional[str] = Query(None)):
    prestadores_filtrados = prestador_repo.buscar(nome=q, servico=servico, local=local)
    todos_servicos = sorted(list(set(s for p in prestador_repo.obter_todos() for s in p.servicos)))
    return templates.TemplateResponse("publico/catalogo.html", {"request": request, "prestadores": prestadores_filtrados, "servicos_disponiveis": todos_servicos, "filtros_ativos": {"q": q, "servico": servico, "local": local}})

# ROTA 2: Perfil do Prestador
@router.get("/perfil/{id_prestador}", response_class=HTMLResponse, name="detalhes_prestador")
async def detalhes_prestador(request: Request, id_prestador: int):
    prestador = prestador_repo.obter_por_id(id_prestador)
    if not prestador: raise HTTPException(status_code=404, detail="Prestador não encontrado")
    return templates.TemplateResponse("publico/perfil_prestador.html", {"request": request, "prestador": prestador})

# ROTA 3: Formulário de Orçamento
@router.get("/perfil/{id_prestador}/orcamento", response_class=HTMLResponse, name="form_solicitar_orcamento")
async def form_solicitar_orcamento(request: Request, id_prestador: int):
    prestador = prestador_repo.obter_por_id(id_prestador)
    if not prestador: raise HTTPException(status_code=404, detail="Prestador não encontrado")
    return templates.TemplateResponse("publico/solicitar_orcamento.html", {"request": request, "prestador": prestador})

# ROTA 4: Envio do Orçamento
@router.post("/perfil/{id_prestador}/orcamento", response_class=HTMLResponse, name="enviar_orcamento")
async def enviar_orcamento(request: Request, id_prestador: int, nome_cliente: str = Form(...), email_cliente: str = Form(...), descricao_servico: str = Form(...)):
    prestador = prestador_repo.obter_por_id(id_prestador)
    if not prestador: raise HTTPException(status_code=404, detail="Prestador não encontrado")
    return templates.TemplateResponse("publico/confirmacao.html", {"request": request, "titulo": "Orçamento Solicitado!", "mensagem": f"Sua solicitação foi enviada para <strong>{prestador.nome}</strong>.", "link_retorno": request.url_for('detalhes_prestador', id_prestador=id_prestador), "texto_retorno": "Voltar ao Perfil"})

# ROTA 5: Formulário de Contratação
@router.get("/perfil/{id_prestador}/contratar", response_class=HTMLResponse, name="form_solicitar_contratacao")
async def form_solicitar_contratacao(request: Request, id_prestador: int):
    prestador = prestador_repo.obter_por_id(id_prestador)
    if not prestador: raise HTTPException(status_code=404, detail="Prestador não encontrado")
    return templates.TemplateResponse("publico/solicitar_contratacao.html", {"request": request, "prestador": prestador})

# ==================================================================
# CORREÇÃO DE SINTAXE APLICADA AQUI
# ==================================================================

# ROTA 6: Envio da Contratação

@router.post("/perfil/{id_prestador}/contratar", response_class=HTMLResponse, name="enviar_contratacao")
async def enviar_contratacao(
    request: Request, 
    id_prestador: int,
    # --- NOVOS CAMPOS ADICIONADOS AQUI ---
    nome_cliente: str = Form(...),
    email_cliente: str = Form(...),
    servico_desejado: str = Form(...),
    detalhes_trabalho: str = Form(...),
    data_inicio: str = Form(...),
    data_fim: str = Form(...),
    localizacao_obra: str = Form(...),
    valor_combinado: float = Form(None), # Opcional, pode não ter sido combinado ainda
    forma_pagamento: str = Form(...)
):
    """
    Recebe os dados do formulário de contratação completo e exibe uma página de confirmação.
    """
    prestador = prestador_repo.obter_por_id(id_prestador)
    if not prestador:
        raise HTTPException(status_code=404, detail="Prestador não encontrado")

    # Em um sistema real, você salvaria todos estes dados em uma tabela "Contratos"
    print("="*30)
    print(f"Nova CONTRATAÇÃO para {prestador.nome}:")
    print(f" - Cliente: {nome_cliente} ({email_cliente})")
    print(f" - Serviço: {servico_desejado}")
    print(f" - Detalhes: {detalhes_trabalho}")
    print(f" - Período: {data_inicio} a {data_fim}")
    print(f" - Local: {localizacao_obra}")
    print(f" - Valor: R$ {valor_combinado if valor_combinado else 'A combinar'}")
    print(f" - Pagamento: {forma_pagamento}")
    print("="*30)
    
    return templates.TemplateResponse("publico/confirmacao.html", {
        "request": request,
        "titulo": "Contratação Solicitada com Sucesso!",
        "mensagem": f"Sua solicitação de contratação para o serviço de <strong>{servico_desejado}</strong> foi enviada para <strong>{prestador.nome}</strong>. Eles entrarão em contato para confirmar os detalhes.",
        "link_retorno": request.url_for('detalhes_prestador', id_prestador=id_prestador),
        "texto_retorno": "Voltar para o Perfil do Prestador"
    })
