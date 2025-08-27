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

# Rota GET para exibir o formulário de login
@router.get("/publico/login")
async def mostrar_login(request: Request):
    return templates.TemplateResponse("publico/login.html", {"request": request})

# Rota POST para processar login
@router.post("/publico/login")
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
        return templates.TemplateResponse("publico/login.html", {"request": request, "mensagem": mensagem})

# Alterar dados de qualquer usuário
@router.post("/publico/perfil/editar/{id}")
async def editar_perfil(request: Request, id: int, nome: str = Form(...), email: str = Form(...), cpf_cnpj: str = Form(None), telefone: str = Form(None), endereco: str = Form(None), tipo_usuario: str = Form(None)):
    usuario = usuario_repo.obter_usuario_por_id(id)
    if usuario:
        usuario.nome = nome
        usuario.email = email
        usuario.cpf_cnpj = cpf_cnpj if cpf_cnpj is not None else usuario.cpf_cnpj
        usuario.telefone = telefone if telefone is not None else usuario.telefone
        usuario.endereco = endereco if endereco is not None else usuario.endereco
        usuario.tipo_usuario = tipo_usuario if tipo_usuario is not None else usuario.tipo_usuario
        usuario_repo.atualizar_usuario(usuario)
        mensagem = "Perfil atualizado com sucesso"
    else:
        mensagem = "Usuário não encontrado"
    return templates.TemplateResponse("publico/perfil.html", {"request": request, "usuario": usuario, "mensagem": mensagem})

# Alterar senha de qualquer usuário
@router.post("/publico/perfil/alterar_senha/{id}")
async def alterar_senha(request: Request, id: int, senha_nova: str = Form(...)):
    usuario = usuario_repo.obter_usuario_por_id(id)
    if usuario:
        usuario_repo.atualizar_senha_usuario(id, senha_nova)
        mensagem = "Senha alterada com sucesso"
    else:
        mensagem = "Usuário não encontrado"
    return templates.TemplateResponse("publico/perfil.html", {"request": request, "usuario": usuario, "mensagem": mensagem})

# Mensagens e responder mensagens (exemplo básico)
@router.get("/publico/mensagens/{id}")
async def ver_mensagens(request: Request, id: int):
    # Busca todas as mensagens onde o usuário é destinatário ou remetente
    todas_mensagens = mensagem_repo.obter_mensagem()
    mensagens = [m for m in todas_mensagens if m.id_destinatario == id or m.id_remetente == id]
    return templates.TemplateResponse("publico/mensagens.html", {"request": request, "mensagens": mensagens})

@router.post("/publico/mensagens/enviar")
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

@router.post("/publico/mensagens/responder/{id}")
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


@router.post("/publico/cadastrar_usuario")
async def cadastrar_usuario(
    request: Request,
    tipo_usuario: str = Form(...),
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    cpf_cnpj: str = Form(None),
    telefone: str = Form(None),
    endereco: str = Form(None),
    genero: str = Form(None),
    data_nascimento: str = Form(None),
    area_atuacao: str = Form(None),
    tipo_pessoa: str = Form(None),
    razao_social: str = Form(None),
    descricao_servicos: str = Form(None)
):
    now = datetime.now()
    if tipo_usuario == "cliente":
        usuario = Cliente(
            id=None,
            nome=nome,
            email=email,
            senha=senha,
            cpf_cnpj=cpf_cnpj,
            telefone=telefone,
            data_cadastro=now,
            endereco=endereco,
            tipo_usuario=tipo_usuario,
            genero=genero,
            data_nascimento=date.fromisoformat(data_nascimento) if data_nascimento else None
        )
        cliente_repo.inserir_cliente(usuario)
        mensagem = "Cliente cadastrado com sucesso"
    elif tipo_usuario == "prestador":
        usuario = Prestador(
            id=None,
            nome=nome,
            email=email,
            senha=senha,
            cpf_cnpj=cpf_cnpj,
            telefone=telefone,
            data_cadastro=now,
            endereco=endereco,
            tipo_usuario=tipo_usuario,
            area_atuacao=area_atuacao,
            tipo_pessoa=tipo_pessoa,
            razao_social=razao_social,
            descricao_servicos=descricao_servicos
        )
        prestador_repo.inserir_prestador(usuario)
        mensagem = "Prestador cadastrado com sucesso"
    elif tipo_usuario == "fornecedor":
        usuario = Fornecedor(
            id=None,
            nome=nome,
            email=email,
            senha=senha,
            cpf_cnpj=cpf_cnpj,
            telefone=telefone,
            data_cadastro=now,
            endereco=endereco,
            tipo_usuario=tipo_usuario,
            razao_social=razao_social
        )
        fornecedor_repo.inserir_fornecedor(usuario)
        mensagem = "Fornecedor cadastrado com sucesso"
    elif tipo_usuario == "admin":
        # cpf_cnpj é obrigatório para admin
        if not cpf_cnpj:
            mensagem = "CPF/CNPJ é obrigatório para administrador"
            usuario = None
        else:
            usuario_base = Usuario(
                id=None,
                nome=nome,
                email=email,
                senha=senha,
                cpf_cnpj=cpf_cnpj,
                telefone=telefone,
                data_cadastro=now,
                endereco=endereco,
                tipo_usuario=tipo_usuario
            )
            id_usuario = usuario_repo.inserir_usuario(usuario_base)
            if id_usuario:
                admin = Administrador(
                    id=None,
                    id_usuario=id_usuario
                )
                administrador_repo.inserir_administrador(admin)
                mensagem = "Administrador cadastrado com sucesso"
                usuario = usuario_base
                usuario.id = id_usuario
            else:
                mensagem = "Erro ao cadastrar administrador"
                usuario = None
    else:
        mensagem = "Tipo de usuário inválido"
        usuario = None
    return templates.TemplateResponse("publico/cadastro_sucesso.html", {"request": request, "mensagem": mensagem, "usuario": usuario})
