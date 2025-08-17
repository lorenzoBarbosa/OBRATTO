from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from data.servico.servico_model import Servico
from data.servico import servico_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates/prestador")

# -------------------------------
# Listar serviços
# -------------------------------
@router.get("/prestador/servicos/listar", name="listar_servicos")
async def listar_servicos(request: Request, id_prestador: int = 1, filtro: str = None):
    try:
        servicos = servico_repo.obter_servico(id_prestador)
        if filtro:
            servicos = [s for s in servicos if filtro.lower() in s.titulo.lower()]
        return templates.TemplateResponse(
            "listar_servicos.html",
            {"request": request, "servicos": servicos, "filtro": filtro, "id_prestador": id_prestador}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "listar_servicos.html",
            {"request": request, "servicos": [], "mensagem": f"Erro ao carregar serviços: {str(e)}", "id_prestador": id_prestador}
        )

# -------------------------------
# Novo serviço (GET e POST)
# -------------------------------
@router.get("/prestador/servicos/novo", name="novo_servico")
async def mostrar_form_novo_servico(request: Request, id_prestador: int = 1):
    return templates.TemplateResponse(
        "servico_form.html", {"request": request, "acao": "novo", "id_prestador": id_prestador}
    )

@router.post("/prestador/servicos/novo", name="processar_novo_servico")
async def adicionar_servico(
    request: Request,
    id_prestador: int = Form(...),
    titulo: str = Form(...),
    descricao: str = Form(...),
    categoria: str = Form(...),
    valor_base: float = Form(...)
):
    try:
        novo_servico = Servico(None, id_prestador, titulo, descricao, categoria, valor_base)
        servico_repo.inserir_servico(novo_servico)
        return RedirectResponse(url=f"/prestador/servicos/listar?id_prestador={id_prestador}", status_code=303)
    except Exception as e:
        return templates.TemplateResponse("servico_form.html", {
            "request": request,
            "acao": "novo",
            "mensagem": f"Erro ao adicionar serviço: {str(e)}",
            "id_prestador": id_prestador
        })

# -------------------------------
# Editar serviço (GET e POST)
# -------------------------------
@router.get("/prestador/servicos/{id}/editar", name="editar_servico")
async def mostrar_form_editar_servico(request: Request, id: int):
    servico = servico_repo.obter_servico_por_id(id)
    if not servico:
        return RedirectResponse(url="/prestador/servicos/listar", status_code=303)
    return templates.TemplateResponse(
        "servico_form.html", {"request": request, "servico": servico, "acao": "editar", "id_prestador": servico.id_prestador}
    )

@router.post("/prestador/servicos/{id}/editar", name="processar_editar_servico")
async def editar_servico(
    request: Request,
    id: int,
    titulo: str = Form(...),
    descricao: str = Form(...),
    categoria: str = Form(...),
    valor_base: float = Form(...)
):
    servico_existente = servico_repo.obter_servico_por_id(id)
    if not servico_existente:
        return RedirectResponse(url="/prestador/servicos/listar", status_code=303)

    try:
        servico_atualizado = Servico(id, servico_existente.id_prestador, titulo, descricao, categoria, valor_base)
        servico_repo.atualizar_servico(servico_atualizado)
        return RedirectResponse(url=f"/prestador/servicos/listar?id_prestador={servico_existente.id_prestador}", status_code=303)
    except Exception as e:
        return templates.TemplateResponse("servico_form.html", {
            "request": request,
            "servico": servico_atualizado,
            "mensagem": f"Erro ao atualizar serviço: {str(e)}",
            "acao": "editar"
        })

# -------------------------------
# Remover serviço
# -------------------------------
@router.post("/prestador/servicos/{id}/remover", name="remover_servico")
async def remover_servico(request: Request, id: int):
    servico = servico_repo.obter_servico_por_id(id)
    if servico:
        servico_repo.deletar_servico(id)
        return RedirectResponse(url=f"/prestador/servicos/listar?id_prestador={servico.id_prestador}", status_code=303)
    return RedirectResponse(url="/prestador/servicos/listar", status_code=303)
