# Salve como: routes/prestador/prestador_router.py

from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates

# ==================================================================
# IMPORTAÇÃO ADICIONADA AQUI
# "Importa a memória de orçamentos que foi criada no roteador público"
# ==================================================================
from routes.publico_router import orcamento_repo

# --- Bloco de Simulação do Serviço (sem alterações) ---
class Servico:
    def __init__(self, id: int, id_prestador: int, titulo: str, descricao: str, categoria: str, valor_base: float, ativo: bool = True):
        self.id, self.id_prestador, self.titulo, self.descricao, self.categoria, self.valor_base, self.ativo = id, id_prestador, titulo, descricao, categoria, valor_base, ativo
class ServicoRepo:
    def __init__(self):
        self._servicos: List[Servico] = [
            Servico(1, 1, "Construção de Parede", "Levantamento de paredes.", "Construção", 1500.00, True),
            Servico(2, 1, "Instalação Elétrica", "Passagem de fiação.", "Elétrica", 3200.50, False),
        ]
        self._next_id = 3
    def obter_servicos_por_prestador(self, id_prestador: int) -> List[Servico]: return [s for s in self._servicos if s.id_prestador == id_prestador]
    def obter_servico_por_id(self, id_servico: int) -> Optional[Servico]: return next((s for s in self._servicos if s.id == id_servico), None)
    def inserir_servico(self, servico: Servico) -> Servico:
        servico.id = self._next_id; self._servicos.append(servico); self._next_id += 1; return servico
    def atualizar_servico(self, id_servico: int, servico_atualizado: Servico):
        for i, s in enumerate(self._servicos):
            if s.id == id_servico: self._servicos[i] = servico_atualizado; return
    def deletar_servico(self, id_servico: int):
        servico = self.obter_servico_por_id(id_servico)
        if servico: self._servicos.remove(servico)
servico_repo = ServicoRepo()
# --- Fim do Bloco de Simulação ---

router = APIRouter(prefix="/prestador", tags=["Prestador"])

# --- Rotas de Navegação e Serviços ---
@router.get("/", response_class=HTMLResponse, name="painel_prestador")
async def painel_prestador(request: Request):
    return templates.TemplateResponse("prestador/painel.html", {"request": request, "id_prestador": 1, "pagina_ativa": "painel"})

@router.get("/servicos", response_class=HTMLResponse, name="listar_servicos")
async def listar_servicos(request: Request, q: Optional[str] = None):
    servicos = servico_repo.obter_servicos_por_prestador(1)
    if q: servicos = [s for s in servicos if q.lower() in s.titulo.lower()]
    return templates.TemplateResponse("prestador/servicos_listar.html", {"request": request, "servicos": servicos, "q": q, "id_prestador": 1, "pagina_ativa": "servicos"})

@router.get("/servicos/novo", response_class=HTMLResponse, name="form_novo_servico")
async def form_novo_servico(request: Request):
    return templates.TemplateResponse("prestador/servico_form.html", {"request": request, "acao": "novo", "id_prestador": 1, "pagina_ativa": "servicos"})

@router.get("/servicos/{id_servico}/editar", response_class=HTMLResponse, name="form_editar_servico")
async def form_editar_servico(request: Request, id_servico: int):
    servico = servico_repo.obter_servico_por_id(id_servico)
    if not servico or servico.id_prestador != 1: raise HTTPException(status_code=404)
    return templates.TemplateResponse("prestador/servico_form.html", {"request": request, "servico": servico, "acao": "editar", "id_prestador": 1, "pagina_ativa": "servicos"})

# (Rotas POST de serviços continuam aqui)
@router.post("/servicos/novo", response_class=RedirectResponse, name="criar_servico")
async def criar_servico(request: Request, id_prestador: int = Form(...), titulo: str = Form(...), descricao: str = Form(...), categoria: str = Form(...), valor_base: float = Form(...)):
    novo_servico = Servico(id=None, id_prestador=id_prestador, titulo=titulo, descricao=descricao, categoria=categoria, valor_base=valor_base)
    servico_repo.inserir_servico(novo_servico)
    return RedirectResponse(url=request.url_for("listar_servicos"), status_code=status.HTTP_303_SEE_OTHER)

@router.post("/servicos/{id_servico}/editar", response_class=RedirectResponse, name="atualizar_servico")
async def atualizar_servico(request: Request, id_servico: int, id_prestador: int = Form(...), titulo: str = Form(...), descricao: str = Form(...), categoria: str = Form(...), valor_base: float = Form(...)):
    servico_existente = servico_repo.obter_servico_por_id(id_servico)
    if not servico_existente or servico_existente.id_prestador != id_prestador: raise HTTPException(status_code=404)
    servico_atualizado = Servico(id_servico, id_prestador, titulo, descricao, categoria, valor_base, servico_existente.ativo)
    servico_repo.atualizar_servico(id_servico, servico_atualizado)
    return RedirectResponse(url=request.url_for("listar_servicos"), status_code=status.HTTP_303_SEE_OTHER)

@router.post("/servicos/{id_servico}/remover", response_class=RedirectResponse, name="remover_servico")
async def remover_servico(request: Request, id_servico: int):
    servico = servico_repo.obter_servico_por_id(id_servico)
    if not servico or servico.id_prestador != 1: raise HTTPException(status_code=404)
    servico_repo.deletar_servico(id_servico)
    return RedirectResponse(url=request.url_for("listar_servicos"), status_code=status.HTTP_303_SEE_OTHER)

@router.get("/agenda", response_class=HTMLResponse, name="agenda_prestador")
async def agenda_prestador(request: Request):
    return templates.TemplateResponse("prestador/agenda.html", {"request": request, "id_prestador": 1, "pagina_ativa": "agenda"})

@router.get("/assinatura", response_class=HTMLResponse, name="assinatura_prestador")
async def assinatura_prestador(request: Request):
    return templates.TemplateResponse("prestador/assinatura.html", {"request": request, "id_prestador": 1, "pagina_ativa": "assinatura"})

# ==================================================================
# ROTA DE SOLICITAÇÕES ATUALIZADA
# ==================================================================
@router.get("/solicitacoes", response_class=HTMLResponse, name="solicitacoes_prestador")
async def solicitacoes_prestador(request: Request):
    id_prestador_logado = 1  # Simulação de qual prestador está logado
    
    # Busca na "memória" todos os orçamentos para este prestador
    solicitacoes = orcamento_repo.obter_por_prestador(id_prestador_logado)
    
    return templates.TemplateResponse("prestador/solicitacoes.html", {
        "request": request,
        "solicitacoes": solicitacoes, # Envia a lista para o HTML
        "id_prestador": id_prestador_logado,
        "pagina_ativa": "solicitacoes"
    })
