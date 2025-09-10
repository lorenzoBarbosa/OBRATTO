from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from data.usuario import usuario_repo
from utils.security import verificar_senha

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/entrar")
async def mostrar_login(request: Request):
    return templates.TemplateResponse("publico/login.html", {"request": request})

# Rota POST para processar login

@router.post("/entrar")
async def processar_login(request: Request, email: str = Form(...), senha: str = Form(...)):
    if not email or not senha:
        return templates.TemplateResponse("publico/login.html", {"request": request, "erro": "Preencha todos os campos."}, status_code=status.HTTP_400_BAD_REQUEST)

    usuario = usuario_repo.obter_usuario_por_email(email)
    if not usuario or not verificar_senha(senha, usuario.senha):
        return templates.TemplateResponse("publico/login.html", {"request": request, "erro": "Email ou senha inválidos"}, status_code=status.HTTP_401_UNAUTHORIZED)

    # Cria sessão completa
    usuario_dict = {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "perfil": getattr(usuario, "perfil", getattr(usuario, "tipo_usuario", "cliente")),
        "foto": getattr(usuario, "foto", None)
    }
    request.session["usuario"] = usuario_dict

    # Redireciona conforme perfil
    perfil = usuario_dict["perfil"].lower()
    if perfil == "admin" or perfil == "administrador":
        return RedirectResponse("/admin", status_code=status.HTTP_303_SEE_OTHER)
    elif perfil == "fornecedor":
        return RedirectResponse("/fornecedor", status_code=status.HTTP_303_SEE_OTHER)
    elif perfil == "cliente":
        return RedirectResponse("/cliente", status_code=status.HTTP_303_SEE_OTHER)
    elif perfil == "prestador":
        return RedirectResponse("/prestador", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
    

@router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)