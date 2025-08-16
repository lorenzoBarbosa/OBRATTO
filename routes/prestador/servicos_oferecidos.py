from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from data.servico.servico_model import Servico
from data.servico import servico_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# -------------------------------
# Listar serviços
# -------------------------------
@router.get("/prestador/servicos/listar")
async def listar_servicos(request: Request, id_prestador: int = 1, filtro: str = None):
    try:
        servicos = servico_repo.obter_servico(id_prestador)
        if filtro:
            servicos = [s for s in servicos if filtro.lower() in s.titulo.lower()]
        return templates.TemplateResponse(
            "prestador/listar_servicos.html",
            {"request": request, "servicos": servicos, "filtro": filtro}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "prestador/listar_servicos.html",
            {"request": request, "servicos": [], "mensagem": f"Erro ao carregar serviços: {str(e)}"}
        )

# -------------------------------
# Adicionar novo serviço (formulário)
# -------------------------------
@router.get("/prestador/servicos/novo")
async def mostrar_form_novo_servico(request: Request):
    return templates.TemplateResponse("prestador/servico_form.html", {"request": request, "acao": "novo"})

# -------------------------------
# Processar novo serviço
# -------------------------------
@router.post("/prestador/servicos/novo")
async def adicionar_servico(
    request: Request,
    id_prestador: int = Form(...),
    titulo: str = Form(...),
    descricao: str = Form(...),
    categoria: str = Form(...),
    valor_base: float = Form(...)
):
    try:
        novo_servico = Servico(
            id_servico=None,  # gerado pelo banco
            id_prestador=id_prestador,
            titulo=titulo,
            descricao=descricao,
            categoria=categoria,
            valor_base=valor_base
        )
        servico_repo.inserir_servico(novo_servico)
        return RedirectResponse(url=f"/prestador/servicos/listar?id_prestador={id_prestador}", status_code=303)
    except Exception as e:
        return templates.TemplateResponse("prestador/servico_form.html", {
            "request": request,
            "acao": "novo",
            "mensagem": f"Erro ao adicionar serviço: {str(e)}"
        })

# -------------------------------
# Editar serviço (formulário)
# -------------------------------
@router.get("/prestador/servicos/{id}/editar")
async def mostrar_form_editar_servico(request: Request, id: int):
    try:
        servico = servico_repo.obter_servico_por_id(id)
        if not servico:
            return RedirectResponse(url="/prestador/servicos/listar", status_code=303)
        return templates.TemplateResponse("prestador/servico_form.html", {"request": request, "servico": servico, "acao": "editar"})
    except Exception as e:
        return templates.TemplateResponse("prestador/servico_form.html", {"request": request, "mensagem": f"Erro: {str(e)}", "acao": "editar"})

# -------------------------------
# Processar edição de serviço
# -------------------------------
@router.post("/prestador/servicos/{id}/editar")
async def editar_servico(
    request: Request,
    id: int,
    titulo: str = Form(...),
    descricao: str = Form(...),
    categoria: str = Form(...),
    valor_base: float = Form(...)
):
    try:
        servico_atualizado = Servico(
            id_servico=id,
            id_prestador=None,  # será obtido do banco, não alteramos
            titulo=titulo,
            descricao=descricao,
            categoria=categoria,
            valor_base=valor_base
        )
        servico_repo.atualizar_servico(servico_atualizado)
        return RedirectResponse(url=f"/prestador/servicos/listar?id_prestador={servico_atualizado.id_prestador}", status_code=303)
    except Exception as e:
        return templates.TemplateResponse("prestador/servico_form.html", {
            "request": request,
            "servico": servico_atualizado,
            "mensagem": f"Erro ao atualizar serviço: {str(e)}",
            "acao": "editar"
        })

# -------------------------------
# Remover serviço
# -------------------------------
@router.post("/prestador/servicos/{id}/remover")
async def remover_servico(request: Request, id: int):
    try:
        servico = servico_repo.obter_servico_por_id(id)
        if servico:
            servico_repo.deletar_servico(id)
            return RedirectResponse(url=f"/prestador/servicos/listar?id_prestador={servico.id_prestador}", status_code=303)
        return RedirectResponse(url="/prestador/servicos/listar", status_code=303)
    except Exception as e:
        return templates.TemplateResponse("prestador/listar_servicos.html", {
            "request": request,
            "mensagem": f"Erro ao deletar serviço: {str(e)}"
        })
    