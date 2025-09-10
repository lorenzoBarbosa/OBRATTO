
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from data.usuario import usuario_repo
from utils.security import verificar_senha

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/publico/login")
async def mostrar_login(request: Request):
    return templates.TemplateResponse("publico/login.html", {"request": request})

# Rota POST para processar login

@router.post("/publico/login")
async def processar_login(request: Request, email: str = Form(...), senha: str = Form(...)):
    # Validação de campos
    if not email or not senha:
        mensagem = "Preencha todos os campos."
        return templates.TemplateResponse("publico/login.html", {"request": request, "mensagem": mensagem}, status_code=status.HTTP_400_BAD_REQUEST)

    usuario = usuario_repo.obter_usuario_por_email(email)
    if usuario:
        # Verificação de senha usando hash seguro
        if verificar_senha(senha, usuario.senha):
            request.session["usuario_id"] = usuario.id
            request.session["tipo_usuario"] = usuario.tipo_usuario
            tipo = usuario.tipo_usuario.lower()
            if tipo == "fornecedor":
                return RedirectResponse(url="/fornecedor", status_code=302)
            elif tipo == "cliente":
                return RedirectResponse(url="/cliente", status_code=302)
            elif tipo == "admin" or tipo == "administrador":
                return RedirectResponse(url="/admin", status_code=302)
            elif tipo == "prestador":
                return RedirectResponse(url="/prestador", status_code=302)
            else:
                return RedirectResponse(url=f"/publico/perfil/{usuario.id}", status_code=302)
        else:
            mensagem = "Usuário ou senha inválidos."
            return templates.TemplateResponse("publico/login.html", {"request": request, "mensagem": mensagem}, status_code=status.HTTP_401_UNAUTHORIZED)
    else:
        mensagem = "Usuário não encontrado. Por favor, cadastre-se."
        return templates.TemplateResponse("publico/login.html", {"request": request, "mensagem": mensagem}, status_code=status.HTTP_404_NOT_FOUND)