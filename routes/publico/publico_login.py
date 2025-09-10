from tempfile import template
from fastapi import Form, Request
from fastapi.responses import RedirectResponse
from websockets import Router

from data.usuario import usuario_repo


@Router.get("/publico/login")
async def mostrar_login(request: Request):
    return template.TemplateResponse("publico/login.html", {"request": request})

# Rota POST para processar login
@Router.post("/publico/login")
async def processar_login(request: Request, email: str = Form(...), senha: str = Form(...)):
    usuario = usuario_repo.obter_usuario_por_email(email)
    if usuario and usuario.senha == senha:
        request.session["usuario_id"] = usuario.id
        request.session["tipo_usuario"] = usuario.tipo_usuario
        # Redirecionamento conforme tipo de usuário
        if usuario.tipo_usuario == "fornecedor":
            return RedirectResponse(url="/fornecedor", status_code=302)
        elif usuario.tipo_usuario == "cliente":
            return RedirectResponse(url="/cliente", status_code=302)
        elif usuario.tipo_usuario == "admin":
            return RedirectResponse(url="/admin", status_code=302)
        elif usuario.tipo_usuario == "prestador":
            return RedirectResponse(url="/prestador", status_code=302)
        else:
            return RedirectResponse(url=f"/publico/perfil/{usuario.id}", status_code=302)
    else:
        mensagem = "E-mail ou senha inválidos"
        return template.TemplateResponse("publico/login.html", {"request": request, "mensagem": mensagem})