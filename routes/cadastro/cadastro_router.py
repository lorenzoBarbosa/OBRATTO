from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from config import templates

router = APIRouter(tags=["Cadastro"])

# ROTA 1: Exibe a página inicial de seleção de cadastro
@router.get("/cadastro", response_class=HTMLResponse, name="pagina_cadastro")
async def pagina_cadastro(request: Request):
    return templates.TemplateResponse("publico/cadastro.html", {"request": request})

# ROTA 2: Exibe o formulário de cadastro de CLIENTE
@router.get("/cadastro/cliente", response_class=HTMLResponse, name="form_cadastro_cliente")
async def form_cadastro_cliente(request: Request):
    return templates.TemplateResponse("publico/cadastro_form.html", {
        "request": request,
        "tipo_perfil": "Cliente",
        "action_url": request.url_for('processar_cadastro_cliente')
    })

# ROTA 3: Exibe o formulário de cadastro de PRESTADOR
@router.get("/cadastro/prestador", response_class=HTMLResponse, name="form_cadastro_prestador")
async def form_cadastro_prestador(request: Request):
    return templates.TemplateResponse("publico/cadastro_form.html", {
        "request": request,
        "tipo_perfil": "Prestador de Serviço",
        "action_url": request.url_for('processar_cadastro_prestador')
    })

# ROTA 4: Exibe o formulário de cadastro de FORNECEDOR
@router.get("/cadastro/fornecedor", response_class=HTMLResponse, name="form_cadastro_fornecedor")
async def form_cadastro_fornecedor(request: Request):
    return templates.TemplateResponse("publico/cadastro_form.html", {
        "request": request,
        "tipo_perfil": "Fornecedor",
        "action_url": request.url_for('processar_cadastro_fornecedor')
    })

# --- ROTAS POST PARA PROCESSAR OS DADOS ---

@router.post("/cadastro/cliente", name="processar_cadastro_cliente")
async def processar_cadastro_cliente(nome: str = Form(...), email: str = Form(...), senha: str = Form(...)):
    # Lógica para salvar o novo cliente no banco de dados
    print(f"NOVO CLIENTE: Nome={nome}, Email={email}")
    return RedirectResponse(url="/cadastro/concluido", status_code=303)

@router.post("/cadastro/prestador", name="processar_cadastro_prestador")
async def processar_cadastro_prestador(nome: str = Form(...), email: str = Form(...), senha: str = Form(...)):
    # Lógica para salvar o novo prestador no banco de dados
    print(f"NOVO PRESTADOR: Nome={nome}, Email={email}")
    return RedirectResponse(url="/cadastro/concluido", status_code=303)

@router.post("/cadastro/fornecedor", name="processar_cadastro_fornecedor")
async def processar_cadastro_fornecedor(nome: str = Form(...), email: str = Form(...), senha: str = Form(...)):
    # Lógica para salvar o novo fornecedor no banco de dados
    print(f"NOVO FORNECEDOR: Nome={nome}, Email={email}")
    return RedirectResponse(url="/cadastro/concluido", status_code=303)

# ROTA FINAL: Página de sucesso
@router.get("/cadastro/concluido", response_class=HTMLResponse, name="cadastro_concluido")
async def cadastro_concluido(request: Request):
    return templates.TemplateResponse("publico/confirmacao.html", {
        "request": request,
        "titulo": "Cadastro Concluído com Sucesso!",
        "mensagem": "Seja bem-vindo(a) à Obratto! Você já pode fazer login para acessar a plataforma.",
        "link_retorno": "/", # Link para a página inicial
        "texto_retorno": "Ir para a Página Inicial"
    })
