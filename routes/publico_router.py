# Salve como: routes/publico_router.py

from fastapi import APIRouter, Request, Query, HTTPException, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Optional, List
from datetime import datetime
from config import templates

# --- Bloco de Simulação de Dados ---

# Em routes/publico_router.py

# ... (importações no topo do arquivo) ...

# ==================================================================
# ATUALIZE A CLASSE PRESTADOR E O REPOSITÓRIO ABAIXO (SEM PORTFÓLIO)
# ==================================================================

class Prestador:
    def __init__(self, id: int, nome: str, area_atuacao: str, avaliacao: float, localizacao: str, logo_url: str, servicos: List[str],
                 # --- Campos Detalhados (sem portfólio) ---
                 descricao: str,
                 telefone: str,
                 email: str
                 ):
        self.id = id
        self.nome = nome
        self.area_atuacao = area_atuacao
        self.avaliacao = avaliacao
        self.localizacao = localizacao
        self.logo_url = logo_url
        self.servicos = servicos
        self.descricao = descricao
        self.telefone = telefone
        self.email = email

class PrestadorRepo:
    def __init__(self):
        self._prestadores: List[Prestador] = [
            Prestador(
                id=1, nome="João Silva Construções", area_atuacao="Construção e Reforma", avaliacao=4.8, localizacao="São Paulo, SP",
                logo_url="/static/img/logos/construção1.jpg",
                servicos=["Alvenaria", "Pintura", "Elétrica", "Reboco", "Fundações"],
                descricao="Com mais de 15 anos de experiência, a João Silva Construções é especialista em reformas residenciais e comerciais, entregando qualidade e pontualidade em cada projeto.",
                telefone="(11) 98765-4321",
                email="contato@joaosilva.com"
            ),
            Prestador(
                id=2, nome="Maria Souza Eletricista", area_atuacao="Elétrica", avaliacao=5.0, localizacao="Rio de Janeiro, RJ",
                logo_url="/static/img/logos/eletricista.jpg",
                servicos=["Instalação Elétrica", "Reparos em Disjuntores", "Troca de Fiação"],
                descricao="Eletricista certificada com foco em segurança e eficiência. Atendimento rápido para emergências e projetos completos.",
                telefone="(21) 91234-5678",
                email="maria.souza@eletro.com"
            ),
            # Adicione os outros prestadores aqui com os novos campos, se desejar
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

# ... (o resto do arquivo continua igual) ...

# ==================================================================
# FIM DO BLOCO A SER SUBSTITUÍDO
# ==================================================================

# ... (O restante do arquivo, incluindo a classe Orcamento e as rotas, continua exatamente igual) ...

# ==================================================================
# NOVO MODELO E REPOSITÓRIO PARA ORÇAMENTOS
# ==================================================================
class Orcamento:
    def __init__(self, id: int, id_prestador: int, nome_cliente: str, email_cliente: str, servico_desejado: str, descricao: str, status: str = "Pendente"):
        self.id = id
        self.id_prestador = id_prestador
        self.nome_cliente = nome_cliente
        self.email_cliente = email_cliente
        self.servico_desejado = servico_desejado
        self.descricao = descricao
        self.status = status
        self.data_solicitacao = datetime.now()

class OrcamentoRepo:
    def __init__(self):
        self._orcamentos: List[Orcamento] = []
        self._next_id = 1
    def salvar(self, orcamento: Orcamento) -> Orcamento:
        orcamento.id = self._next_id
        self._orcamentos.append(orcamento)
        self._next_id += 1
        print(f"Orçamento #{orcamento.id} para prestador #{orcamento.id_prestador} salvo com sucesso.")
        return orcamento
    def obter_por_prestador(self, id_prestador: int) -> List[Orcamento]:
        return [o for o in self._orcamentos if o.id_prestador == id_prestador]

# Instância global para ser acessada por outros roteadores
orcamento_repo = OrcamentoRepo()

# No topo do routes/publico_router.py
from datetime import datetime, timedelta # Adicione esta importação

# ... (código existente até a instância orcamento_repo) ...
orcamento_repo = OrcamentoRepo()

class Contratacao:
    def __init__(self, id: int, prestador_nome: str, servico: str, data_inicio: datetime, status: str, valor: float):
        self.id = id
        self.prestador_nome = prestador_nome
        self.servico = servico
        self.data_inicio = data_inicio
        self.status = status # "Em andamento", "Concluído", "Cancelado"
        self.valor = valor

class SolicitacaoPendente:
    def __init__(self, id: int, prestador_nome: str, servico: str, data_solicitacao: datetime, status: str):
        self.id = id
        self.prestador_nome = prestador_nome
        self.servico = servico
        self.data_solicitacao = data_solicitacao
        self.status = status # "Aguardando resposta", "Visualizado"

class ClienteRepo:
    def __init__(self):
        self._contratacoes: List[Contratacao] = [
            Contratacao(1, "João Silva Construções", "Construção de Parede", datetime.now() - timedelta(days=10), "Em andamento", 1500.00),
            Contratacao(2, "Pedro Pinturas", "Pintura Interna", datetime.now() - timedelta(days=30), "Concluído", 850.00),
        ]
        self._solicitacoes: List[SolicitacaoPendente] = [
            SolicitacaoPendente(1, "Maria Souza Eletricista", "Instalação Elétrica", datetime.now() - timedelta(days=2), "Aguardando resposta"),
            SolicitacaoPendente(2, "Hidráulica Rápida Ltda", "Caça Vazamento", datetime.now() - timedelta(days=1), "Visualizado"),
        ]
    def obter_contratacoes_por_cliente(self, id_cliente: int) -> List[Contratacao]:
        return self._contratacoes
    def obter_solicitacoes_por_cliente(self, id_cliente: int) -> List[SolicitacaoPendente]:
        return self._solicitacoes

cliente_repo = ClienteRepo()
# --- Fim do Bloco de Simulação --.


router = APIRouter(tags=["Público"])

# ROTA 1: Catálogo (sem alterações)
@router.get("/catalogo", response_class=HTMLResponse, name="catalogo_prestadores")
async def catalogo_prestadores(request: Request, q: Optional[str] = Query(None), servico: Optional[str] = Query(None), local: Optional[str] = Query(None)):
    prestadores_filtrados = prestador_repo.buscar(nome=q, servico=servico, local=local)
    todos_servicos = sorted(list(set(s for p in prestador_repo.obter_todos() for s in p.servicos)))
    return templates.TemplateResponse("publico/catalogo.html", {"request": request, "prestadores": prestadores_filtrados, "servicos_disponiveis": todos_servicos, "filtros_ativos": {"q": q, "servico": servico, "local": local}})

# ROTA 2: Perfil do Prestador (sem alterações)
@router.get("/perfil/{id_prestador}", response_class=HTMLResponse, name="detalhes_prestador")
async def detalhes_prestador(request: Request, id_prestador: int):
    prestador = prestador_repo.obter_por_id(id_prestador)
    if not prestador: raise HTTPException(status_code=404, detail="Prestador não encontrado")
    return templates.TemplateResponse("publico/perfil_prestador.html", {"request": request, "prestador": prestador})

# ROTA 3: Formulário de Orçamento (sem alterações)
@router.get("/perfil/{id_prestador}/orcamento", response_class=HTMLResponse, name="form_solicitar_orcamento")
async def form_solicitar_orcamento(request: Request, id_prestador: int):
    prestador = prestador_repo.obter_por_id(id_prestador)
    if not prestador: raise HTTPException(status_code=404, detail="Prestador não encontrado")
    return templates.TemplateResponse("publico/solicitar_orcamento.html", {"request": request, "prestador": prestador})

# ==================================================================
# ROTA 4 ATUALIZADA PARA SALVAR O ORÇAMENTO
# ==================================================================
@router.post("/perfil/{id_prestador}/orcamento", response_class=HTMLResponse, name="enviar_orcamento")
async def enviar_orcamento(
    request: Request, 
    id_prestador: int,
    nome_cliente: str = Form(...),
    email_cliente: str = Form(...),
    servico_desejado: str = Form(...),
    descricao_servico: str = Form(...),
    anexos: List[UploadFile] = File([])
):
    prestador = prestador_repo.obter_por_id(id_prestador)
    if not prestador: raise HTTPException(status_code=404, detail="Prestador não encontrado")

    nova_solicitacao = Orcamento(
        id=None,
        id_prestador=id_prestador,
        nome_cliente=nome_cliente,
        email_cliente=email_cliente,
        servico_desejado=servico_desejado,
        descricao=descricao_servico
    )
    orcamento_repo.salvar(nova_solicitacao)

    for anexo in anexos:
        if anexo.filename:
            print(f"Arquivo recebido: {anexo.filename} ({anexo.content_type})")

    return templates.TemplateResponse("publico/confirmacao.html", {
        "request": request,
        "titulo": "Orçamento Solicitado com Sucesso!",
        "mensagem": f"Sua solicitação para o serviço de <strong>{servico_desejado}</strong> foi enviada para <strong>{prestador.nome}</strong>. Você será notificado por e-mail quando ele responder.",
        "link_retorno": request.url_for('detalhes_prestador', id_prestador=id_prestador),
        "texto_retorno": "Voltar para o Perfil do Prestador"
    })

# ROTA 5: Formulário de Contratação (sem alterações)
@router.get("/perfil/{id_prestador}/contratar", response_class=HTMLResponse, name="form_solicitar_contratacao")
async def form_solicitar_contratacao(request: Request, id_prestador: int):
    prestador = prestador_repo.obter_por_id(id_prestador)
    if not prestador: raise HTTPException(status_code=404, detail="Prestador não encontrado")
    return templates.TemplateResponse("publico/solicitar_contratacao.html", {"request": request, "prestador": prestador})

# ROTA 6: Envio da Contratação (sem alterações)
@router.post("/perfil/{id_prestador}/contratar", response_class=HTMLResponse, name="enviar_contratacao")
async def enviar_contratacao(
    request: Request, id_prestador: int, nome_cliente: str = Form(...), email_cliente: str = Form(...),
    servico_desejado: str = Form(...), detalhes_trabalho: str = Form(...), data_inicio: str = Form(...),
    data_fim: str = Form(...), localizacao_obra: str = Form(...), valor_combinado: float = Form(None),
    forma_pagamento: str = Form(...)
):
    prestador = prestador_repo.obter_por_id(id_prestador)
    if not prestador: raise HTTPException(status_code=404, detail="Prestador não encontrado")
    print("="*30); print(f"Nova CONTRATAÇÃO para {prestador.nome}:"); print(f" - Cliente: {nome_cliente} ({email_cliente})"); print(f" - Serviço: {servico_desejado}"); print(f" - Detalhes: {detalhes_trabalho}"); print(f" - Período: {data_inicio} a {data_fim}"); print(f" - Local: {localizacao_obra}"); print(f" - Valor: R$ {valor_combinado if valor_combinado else 'A combinar'}"); print(f" - Pagamento: {forma_pagamento}"); print("="*30)
    return templates.TemplateResponse("publico/confirmacao.html", {"request": request, "titulo": "Contratação Solicitada com Sucesso!", "mensagem": f"Sua solicitação de contratação para o serviço de <strong>{servico_desejado}</strong> foi enviada para <strong>{prestador.nome}</strong>. Eles entrarão em contato para confirmar os detalhes.", "link_retorno": request.url_for('detalhes_prestador', id_prestador=id_prestador), "texto_retorno": "Voltar para o Perfil do Prestador"})

# Adicione estas duas rotas ao final do routes/publico_router.py


@router.get("/minhas-contratacoes", response_class=HTMLResponse, name="minhas_contratacoes")
async def minhas_contratacoes(request: Request):
    id_cliente_logado = 1 # Simulação
    contratacoes = cliente_repo.obter_contratacoes_por_cliente(id_cliente_logado)
    return templates.TemplateResponse("publico/minhas_contratacoes.html", {
        "request": request,
        "contratacoes": contratacoes
    })

@router.get("/minhas-solicitacoes", response_class=HTMLResponse, name="minhas_solicitacoes")
async def minhas_solicitacoes(request: Request):
    id_cliente_logado = 1 # Simulação
    solicitacoes = cliente_repo.obter_solicitacoes_por_cliente(id_cliente_logado)
    return templates.TemplateResponse("publico/minhas_solicitacoes.html", {
        "request": request,
        "solicitacoes": solicitacoes
    })
