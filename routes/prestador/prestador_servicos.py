from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates
from data.servico import servico_repo

router = APIRouter()

# Rota para listar serviços do Prestador 
@router.get("/servicos")
async def listar_servicos(request: Request, q: Optional[str] = None):
    return templates.TemplateResponse("prestador/servicos_listar.html", {"request": request})

# Rota para cadastrar novo serviço
@router.get("/servicos/novo")
async def form_novo_servico(request: Request):
    return templates.TemplateResponse("prestador/servico_form.html", {"request": request})

# Rota post para cadastrar novo serviço
@router.post("/servicos/novo", name="cadastrar_novo_servico")
async def cadastrar_novo_servico(
    request: Request,
    id_prestador: int = Form(...),      
    titulo: str = Form(...),      
    descricao: str = Form(...),
    categoria: str = Form(...)         
    valor: float = Form(...)            
    ):
    id_servico: int
    id_prestador: int
    titulo: str
    descricao: str
    categoria: str
    valor_base: float
    nome_prestador: Optional[str] = None




    contexto = {"request": request}
    
    try:
        novo_servico = servico_repo.criar_servico(
            id_prestador=id_prestador,
            nome=nome_servico,
            descricao=descricao,
            valor=valor
        )

        if novo_servico:
            contexto["mensagem"] = f"Serviço '{novo_servico.nome}' cadastrado com sucesso!"
            contexto["sucesso"] = True
        else:
            contexto["mensagem"] = "Não foi possível cadastrar o serviço. Verifique os dados e tente novamente."
            contexto["sucesso"] = False

    except Exception as e:
        print(f"Erro inesperado ao cadastrar serviço: {e}") 
        contexto["mensagem"] = "Ocorreu um erro inesperado ao tentar cadastrar o serviço."
        contexto["sucesso"] = False
    return templates.TemplateResponse("prestador/servico_form.html", contexto)


# Rota para editar serviço 
@router.get("/servicos/editar/{id_servico}")
async def form_editar_servico(request: Request, id_servico: int):
    return templates.TemplateResponse("prestador/servico_form.html", {"request": request})

# Rota para remover serviço
@router.get("/servicos/remover/{id_servico}")
async def remover_servico(request: Request):
    return templates.TemplateResponse("prestador/servico_excluir.html", {"request": request})