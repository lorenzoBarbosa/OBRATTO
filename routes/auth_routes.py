# from fastapi import APIRouter, Request, Form, HTTPException, status
# from fastapi.responses import HTMLResponse, RedirectResponse
# from typing import Optional, List
# from config import templates


# # Rota de Login:
# @router.post("/login")
# async def post_login(
#     request: Request,
#     email: str = Form(...),
#     senha: str = Form(...),
#     redirect: str = Form(None)
# ):
#     usuario = usuario_repo.obter_por_email(email)
    
#     if not usuario or not verificar_senha(senha, usuario.senha):
#         return templates.TemplateResponse(
#             "login.html",
#             {"request": request, "erro": "Email ou senha inválidos"}
#         )
    
#     # Criar sessão
#     usuario_dict = {
#         "id": usuario.id,
#         "nome": usuario.nome,
#         "email": usuario.email,
#         "perfil": usuario.perfil,
#         "foto": usuario.foto
#     }
#     criar_sessao(request, usuario_dict)
    
#     # Redirecionar
#     if redirect:
#         return RedirectResponse(redirect, status.HTTP_303_SEE_OTHER)
    
#     if usuario.perfil == "admin":
#         return RedirectResponse("/admin", status.HTTP_303_SEE_OTHER)
    
#     return RedirectResponse("/", status.HTTP_303_SEE_OTHER)
# ```

# **Rota de Logout:**
# ```python
# @router.get("/logout")
# async def logout(request: Request):
#     request.session.clear()
#     return RedirectResponse("/", status.HTTP_303_SEE_OTHER)
# ```

# **Rota de Cadastro:**
# ```python
# @router.post("/cadastro")
# async def post_cadastro(
#     request: Request,
#     nome: str = Form(...),
#     email: str = Form(...),
#     senha: str = Form(...),
#     cpf: str = Form(None),
#     telefone: str = Form(None)
# ):
#     # Verificar se email já existe
#     if usuario_repo.obter_por_email(email):
#         return templates.TemplateResponse(
#             "cadastro.html",
#             {"request": request, "erro": "Email já cadastrado"}
#         )
    
#     # Criar hash da senha
#     senha_hash = criar_hash_senha(senha)
    
#     # Criar usuário
#     usuario = Usuario(
#         id=0,
#         nome=nome,
#         email=email,
#         senha=senha_hash,
#         perfil="cliente"
#     )
    
#     usuario_id = usuario_repo.inserir(usuario)
    
#     # Se tiver CPF/telefone, inserir na tabela cliente
#     if cpf and telefone:
#         cliente = Cliente(
#             id=usuario_id,
#             cpf=cpf,
#             telefone=telefone
#         )
#         cliente_repo.inserir(cliente)
    
#     return RedirectResponse("/login", status.HTTP_303_SEE_OTHER)
# ```