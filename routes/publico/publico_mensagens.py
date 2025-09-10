from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from data.usuario.usuario_model import Usuario
from data.usuario import usuario_repo
from data.cliente.cliente_model import Cliente
from data.cliente import cliente_repo
from data.prestador.prestador_model import Prestador
from data.prestador import prestador_repo
from data.fornecedor.fornecedor_model import Fornecedor
from data.fornecedor import fornecedor_repo
from data.administrador.administrador_model import Administrador
from data.administrador import administrador_repo
from data.mensagem.mensagem_model import Mensagem
from data.mensagem import mensagem_repo
from datetime import date, datetime

router = APIRouter()
templates = Jinja2Templates(directory="templates")



# Mensagens e responder mensagens (exemplo básico)
@router.get("/publico/mensagens/{id}")
async def ver_mensagens(request: Request, id: int):
    # Busca todas as mensagens onde o usuário é destinatário ou remetente
    todas_mensagens = mensagem_repo.obter_mensagem()
    mensagens = [m for m in todas_mensagens if m.id_destinatario == id or m.id_remetente == id]
    return templates.TemplateResponse("publico/mensagens.html", {"request": request, "mensagens": mensagens})

@router.post("/enviar")
async def enviar_mensagem(request: Request, id_remetente: int = Form(...), id_destinatario: int = Form(...), conteudo: str = Form(...), nome_remetente: str = Form(...), nome_destinatario: str = Form(...)):
    mensagem = Mensagem(
        id_mensagem=None,
        id_remetente=id_remetente,
        id_destinatario=id_destinatario,
        conteudo=conteudo,
        data_hora=datetime.now(),
        nome_remetente=nome_remetente,
        nome_destinatario=nome_destinatario
    )
    mensagem_repo.inserir_mensagem(mensagem)
    mensagem_texto = "Mensagem enviada com sucesso"
    return templates.TemplateResponse("publico/mensagens.html", {"request": request, "mensagem": mensagem_texto})

@router.post("/responder/{id}")
async def responder_mensagem(request: Request, id: int, resposta: str = Form(...), nome_remetente: str = Form(...), nome_destinatario: str = Form(...)):
    mensagem_original = mensagem_repo.obter_mensagem_por_id(id)
    if mensagem_original:
        mensagem = Mensagem(
            id_mensagem=None,
            id_remetente=mensagem_original.id_destinatario,
            id_destinatario=mensagem_original.id_remetente,
            conteudo=resposta,
            data_hora=datetime.now(),
            nome_remetente=nome_remetente,
            nome_destinatario=nome_destinatario
        )
        mensagem_repo.inserir_mensagem(mensagem)
        mensagem_texto = "Resposta enviada com sucesso"
    else:
        mensagem_texto = "Mensagem original não encontrada"
    return templates.TemplateResponse("publico/mensagens.html", {"request": request, "mensagem": mensagem_texto})



