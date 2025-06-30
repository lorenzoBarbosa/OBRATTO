import sys
import os

from data.anuncio.anuncio_repo import *
from data.fornecedor.fornecedor_repo import *
from data.usuario.usuario_repo import *


def test_criar_tabela_anuncio(self, db):
    # Arrange preparar para o teste
    criar_tabela_usuario()
    criar_tabela_fornecedor()
    # Act fazer a ação que será testada
    resultado = criar_tabela_anuncio()
    # Asserts verificar se o resultado é o esperado
    assert resultado is True, "A tabela de anúncios não foi criada com sucesso."

def test_inserir_anuncio(self, db):
    # Arrange preparar para o teste
    criar_tabela_usuario()
    criar_tabela_fornecedor()
    criar_tabela_anuncio()
    
    usuario = Usuario(0, nome="Teste", email="dsiufu", senha="123456", cpf_cnpj="12345678901", telefone="1234567890", data_cadastro="2023-10-01", endereco="Rua Teste, 123")
    id_usuario = inserir_usuario(usuario)
    fornecedor = Fornecedor(0,"","","","","","","", "Obratto")
    id_fornecedor = inserir_fornecedor(fornecedor, id_usuario)
    anuncio = Anuncio(0, nome_anuncio="Anúncio Teste", id_fornecedor=id_fornecedor, data_criacao="2023-10-01", descricao="Descrição do anúncio", preco=100.0)
    # Act fazer a ação que será testada
    id_anuncio = inserir_anuncio(anuncio)
    anuncio_db = obter_anuncio_por_nome("Anúncio Teste")
    # Asserts verificar se o resultado é o esperado
    assert id_anuncio is not None, "O anúncio não foi inserido com sucesso."
    assert anuncio_db is not None, "O anúncio não foi encontrado no banco de dados."
    assert anuncio_db.nome_anuncio == "Anúncio Teste", "O nome do anúncio não corresponde ao esperado."
    assert anuncio_db.preco == 100.0, "O preço do anúncio não corresponde ao esperado."
    assert anuncio_db.descricao == "Descrição do anúncio", "A descrição do anúncio não corresponde ao esperado."
    assert anuncio_db.id_fornecedor == id_fornecedor, "O fornecedor do anúncio não corresponde ao esperado."
    assert anuncio_db.data_criacao == "2023-10-01", "A data de criação do anúncio não corresponde ao esperado."

def test_obter_todos_anuncios(self, db):
    # Arrange preparar para o teste
    criar_tabela_usuario()
    criar_tabela_fornecedor()
    criar_tabela_anuncio()

    usuario = Usuario(0, nome="Teste", email="dsiufu", senha="123456", cpf_cnpj="12345678901", telefone="1234567890", data_cadastro="2023-10-01", endereco="Rua Teste, 123")
    id_usuario = inserir_usuario(usuario)
    fornecedor = Fornecedor(0,"","","","","","","", "Obratto")
    id_fornecedor = inserir_fornecedor(fornecedor, id_usuario)
    anuncio = Anuncio(0, nome_anuncio="Anúncio Teste", id_fornecedor=id_fornecedor, data_criacao="2023-10-01", descricao="Descrição do anúncio", preco=100.0)
    # Act fazer a ação que será testada
    id_anuncio = inserir_anuncio(anuncio)
    anuncios = obter_todos_anuncios()
    anuncio_db = next((a for a in anuncios if a.nome_anuncio == "Anúncio Teste"), None)
    # Asserts verificar se o resultado é o esperado
    assert id_anuncio is not None, "O anúncio não foi inserido com sucesso."
    assert anuncio_db is not None, "O anúncio não foi encontrado no banco de dados."
    assert anuncio_db.nome_anuncio == "Anúncio Teste", "O nome do anúncio não corresponde ao esperado."
    assert anuncio_db.preco == 100.0, "O preço do anúncio não corresponde ao esperado."
    assert anuncio_db.descricao == "Descrição do anúncio", "A descrição do anúncio não corresponde ao esperado."
    assert anuncio_db.id_fornecedor == id_fornecedor, "O fornecedor do anúncio não corresponde ao esperado."
    assert anuncio_db.data_criacao == "2023-10-01", "A data de criação do anúncio não corresponde ao esperado."

def test_obter_anuncio_por_nome(self, db):
    # Arrange preparar para o teste
    criar_tabela_usuario()
    criar_tabela_fornecedor()
    criar_tabela_anuncio()

    usuario = Usuario(0, nome="Teste", email="dsiufu", senha="123456", cpf_cnpj="12345678901", telefone="1234567890", data_cadastro="2023-10-01", endereco="Rua Teste, 123")
    id_usuario = inserir_usuario(usuario)
    fornecedor = Fornecedor(0,"","","","","","","", "Obratto")
    id_fornecedor = inserir_fornecedor(fornecedor, id_usuario)
    anuncio = Anuncio(0, nome_anuncio="Anúncio Teste", id_fornecedor=id_fornecedor, data_criacao="2023-10-01", descricao="Descrição do anúncio", preco=100.0)
    # Act fazer a ação que será testada
    id_anuncio = inserir_anuncio(anuncio)
    anuncio_db = obter_anuncio_por_nome("Anúncio Teste")
    # Asserts verificar se o resultado é o esperado
    assert id_anuncio is not None, "O anúncio não foi inserido com sucesso."
    assert anuncio_db is not None, "O anúncio não foi encontrado no banco de dados."
    assert anuncio_db.nome_anuncio == "Anúncio Teste", "O nome do anúncio não corresponde ao esperado."
    assert anuncio_db.preco == 100.0, "O preço do anúncio não corresponde ao esperado."
    assert anuncio_db.descricao == "Descrição do anúncio", "A descrição do anúncio não corresponde ao esperado."
    assert anuncio_db.id_fornecedor == id_fornecedor, "O fornecedor do anúncio não corresponde ao esperado."
    assert anuncio_db.data_criacao == "2023-10-01", "A data de criação do anúncio não corresponde ao esperado."

def test_obter_anuncio_por_id(self, db):
     # Arrange preparar para o teste
    criar_tabela_usuario()
    criar_tabela_fornecedor()
    criar_tabela_anuncio()

    usuario = Usuario(0, nome="Teste", email="dsiufu", senha="123456", cpf_cnpj="12345678901", telefone="1234567890", data_cadastro="2023-10-01", endereco="Rua Teste, 123")
    id_usuario = inserir_usuario(usuario)
    fornecedor = Fornecedor(0,"","","","","","","", "Obratto")
    id_fornecedor = inserir_fornecedor(fornecedor, id_usuario)
    anuncio = Anuncio(0, nome_anuncio="Anúncio Teste", id_fornecedor=id_fornecedor, data_criacao="2023-10-01", descricao="Descrição do anúncio", preco=100.0)
    # Act fazer a ação que será testada
    id_anuncio = inserir_anuncio(anuncio)
    anuncio_db = obter_anuncio_por_id(id_anuncio)
    # Asserts verificar se o resultado é o esperado
    assert id_anuncio is not None, "O anúncio não foi inserido com sucesso."
    assert anuncio_db is not None, "O anúncio não foi encontrado no banco de dados."
    assert anuncio_db.nome_anuncio == "Anúncio Teste", "O nome do anúncio não corresponde ao esperado."
    assert anuncio_db.preco == 100.0, "O preço do anúncio não corresponde ao esperado."
    assert anuncio_db.descricao == "Descrição do anúncio", "A descrição do anúncio não corresponde ao esperado."
    assert anuncio_db.id_fornecedor == id_fornecedor, "O fornecedor do anúncio não corresponde ao esperado."
    assert anuncio_db.data_criacao == "2023-10-01", "A data de criação do anúncio não corresponde ao esperado."

def test_atualizar_anuncio_por_nome(self, db):
    id_anuncio, id_fornecedor = ()
    atualizar_anuncio_por_nome("Atualizar anuncio", novo_preco=200.0)
    anuncio_db = obter_anuncio_por_nome("Anúncio Teste")
    assert anuncio_db is not None
    

def test_deletar_anuncio(self, db):
    id_anuncio, id_fornecedor = ()
    deletar_anuncio("Anúncio Teste")
    anuncio_db = obter_anuncio_por_nome("Anúncio Teste")
    assert anuncio_db is None

