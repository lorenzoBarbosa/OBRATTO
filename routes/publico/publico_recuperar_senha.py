from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from data.usuario import usuario_repo
from utils.security import gerar_token, criar_hash_senha

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/recuperar-senha")
async def recuperar_senha_get(request: Request):
    return templates.TemplateResponse("publico/recuperar_senha.html", {"request": request})

@router.post("/recuperar-senha")
async def recuperar_senha_post(request: Request, email: str = Form(...)):
    usuario = usuario_repo.obter_usuario_por_email(email)
    if usuario:
        # Gera token e salva no usuário
        token = gerar_token()
        usuario.token_redefinicao = token
        usuario_repo.atualizar_usuario(usuario)
        # Aqui você enviaria o e-mail real. Exemplo:
        link = f"http://localhost:8000/publico/resetar-senha?token={token}"
        mensagem = f"Enviamos um link de recuperação para o e-mail: {email}. (Simulação: {link})"
    else:
        mensagem = "E-mail não encontrado."
    return templates.TemplateResponse("publico/recuperar_senha.html", {"request": request, "mensagem": mensagem})

@router.get("/resetar-senha")
async def resetar_senha_get(request: Request, token: str):
    return templates.TemplateResponse("publico/redefinir_senha.html", {"request": request, "token": token})

@router.post("/resetar-senha")
async def resetar_senha_post(request: Request, token: str = Form(...), nova_senha: str = Form(...)):
    usuario = usuario_repo.obter_usuario_por_token(token)
    if usuario:
        usuario.senha = criar_hash_senha(nova_senha)
        usuario.token_redefinicao = None
        usuario_repo.atualizar_usuario(usuario)
        mensagem = "Senha redefinida com sucesso! Faça login."
        return RedirectResponse("/publico/login", status_code=303)
    else:
        mensagem = "Token inválido ou expirado."
        return templates.TemplateResponse("publico/redefinir_senha.html", {"request": request, "mensagem": mensagem, "token": token})
