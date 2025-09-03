from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from data.cartao.cartao_model import CartaoCredito
from data.cartao.cartao_repo import CartaoRepository

cartao_repo = CartaoRepository()
router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Listar cartões
@router.get("/cartoes")
async def listar_cartoes(request: Request, id_usuario: int = 1):
	cartoes = cartao_repo.obter_cartoes_fornecedor(id_usuario)
	return templates.TemplateResponse("publico/pagamento/meus_cartoes.html", {
		"request": request,
		"cartoes": cartoes,
		"id_fornecedor": id_usuario
	})

# Mostrar formulário para adicionar cartão
@router.get("/cartoes/adicionar")
async def mostrar_adicionar_cartao(request: Request, id_usuario: int = 1):
	return templates.TemplateResponse("publico/pagamento/adicionar_cartao.html", {
		"request": request,
		"id_fornecedor": id_usuario
	})

# Processar adição de cartão
@router.post("/cartoes/adicionar")
async def adicionar_cartao(
	request: Request,
	id_usuario: int = Form(...),
	numero_cartao: str = Form(...),
	nome_titular: str = Form(...),
	mes_vencimento: str = Form(...),
	ano_vencimento: str = Form(...),
	apelido: str = Form(...),
	principal: str = Form(None)
):
	try:
		resultado = cartao_repo.criar_cartao_from_form(
			id_fornecedor=id_usuario,
			numero_cartao=numero_cartao,
			nome_titular=nome_titular,
			mes_vencimento=mes_vencimento,
			ano_vencimento=ano_vencimento,
			apelido=apelido,
			principal=(principal == "true")
		)
		if resultado:
			return RedirectResponse(url="/publico/pagamento/cartoes", status_code=303)
		else:
			return templates.TemplateResponse("publico/pagamento/adicionar_cartao.html", {
				"request": request,
				"id_fornecedor": id_usuario,
				"mensagem": "Erro ao salvar o cartão. Tente novamente."
			})
	except Exception as e:
		return templates.TemplateResponse("publico/pagamento/adicionar_cartao.html", {
			"request": request,
			"id_fornecedor": id_usuario,
			"mensagem": f"Erro ao processar cartão: {str(e)}"
		})

# Mostrar formulário para editar cartão
@router.get("/cartoes/editar/{id_cartao}")
async def mostrar_editar_cartao(request: Request, id_cartao: int, id_usuario: int = 1):
	cartao = cartao_repo.obter_cartao_por_id(id_cartao)
	if not cartao or cartao.id_fornecedor != id_usuario:
		return RedirectResponse(url="/publico/pagamento/cartoes", status_code=303)
	return templates.TemplateResponse("publico/pagamento/adicionar_cartao.html", {
		"request": request,
		"cartao": cartao,
		"id_fornecedor": id_usuario
	})

# Processar edição de cartão
@router.post("/cartoes/editar/{id_cartao}")
async def editar_cartao(
	request: Request,
	id_cartao: int,
	id_usuario: int = Form(...),
	nome_titular: str = Form(...),
	apelido: str = Form(...),
	principal: str = Form(None)
):
	try:
		cartao = cartao_repo.obter_cartao_por_id(id_cartao)
		if not cartao or cartao.id_fornecedor != id_usuario:
			return RedirectResponse(url="/publico/pagamento/cartoes", status_code=303)
		cartao.nome_titular = nome_titular.strip().upper()
		cartao.apelido = apelido.strip()
		cartao.principal = (principal == "true")
		resultado = cartao_repo.atualizar_cartao(cartao)
		if resultado:
			return RedirectResponse(url="/publico/pagamento/cartoes", status_code=303)
		else:
			return templates.TemplateResponse("publico/pagamento/adicionar_cartao.html", {
				"request": request,
				"cartao": cartao,
				"id_fornecedor": id_usuario,
				"mensagem": "Erro ao atualizar o cartão. Tente novamente."
			})
	except Exception as e:
		return templates.TemplateResponse("publico/pagamento/adicionar_cartao.html", {
			"request": request,
			"cartao": cartao if 'cartao' in locals() else None,
			"id_fornecedor": id_usuario,
			"mensagem": f"Erro ao processar alterações: {str(e)}"
		})

# Mostrar confirmação de exclusão
@router.get("/cartoes/excluir/{id_cartao}")
async def mostrar_confirmar_exclusao(request: Request, id_cartao: int, id_usuario: int = 1):
	cartao = cartao_repo.obter_cartao_por_id(id_cartao)
	if not cartao or cartao.id_fornecedor != id_usuario:
		return RedirectResponse(url="/publico/pagamento/cartoes", status_code=303)
	return templates.TemplateResponse("publico/pagamento/confirmar_exclusao_cartao.html", {
		"request": request,
		"cartao": cartao
	})

# Processar exclusão de cartão
@router.post("/cartoes/excluir/{id_cartao}")
async def excluir_cartao(request: Request, id_cartao: int, id_usuario: int = 1):
	try:
		cartao = cartao_repo.obter_cartao_por_id(id_cartao)
		if not cartao or cartao.id_fornecedor != id_usuario:
			return RedirectResponse(url="/publico/pagamento/cartoes", status_code=303)
		resultado = cartao_repo.remover_cartao(id_cartao)
		if resultado:
			return RedirectResponse(url="/publico/pagamento/cartoes", status_code=303)
		else:
			return templates.TemplateResponse("publico/pagamento/confirmar_exclusao_cartao.html", {
				"request": request,
				"cartao": cartao,
				"mensagem": "Erro ao excluir o cartão. Tente novamente."
			})
	except Exception as e:
		return templates.TemplateResponse("publico/pagamento/confirmar_exclusao_cartao.html", {
			"request": request,
			"cartao": cartao if 'cartao' in locals() else None,
			"mensagem": f"Erro ao processar exclusão: {str(e)}"
		})

# Definir cartão como principal
@router.post("/cartoes/definir_principal")
async def definir_cartao_principal(request: Request, id_cartao: int = Form(...), id_usuario: int = 1):
	cartao = cartao_repo.obter_cartao_por_id(id_cartao)
	if not cartao or cartao.id_fornecedor != id_usuario:
		return RedirectResponse(url="/publico/pagamento/cartoes", status_code=303)
	cartao_repo.definir_todos_nao_principal(id_usuario)
	cartao.principal = True
	cartao_repo.atualizar_cartao(cartao)
	return RedirectResponse(url="/publico/pagamento/cartoes", status_code=303)
