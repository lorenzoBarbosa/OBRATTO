
from typing import Optional
import pytest
import sqlite3
from datetime import date, datetime
from utils.db import open_connection


from data.usuario.usuario_model import Usuario
from data.usuario.usuario_repo import criar_tabela_usuario, inserir_usuario

from data.cliente.cliente_model import Cliente
from data.cliente.cliente_repo import atualizar_cliente, criar_tabela_cliente, deletar_cliente, inserir_cliente, obter_cliente, obter_cliente_por_id



class TestAdministradorRepo:

    def test_criar_tabela_cliente(self, test_db):
        #Arrange
        #Act
        resultado = criar_tabela_cliente()
        #Assert
        assert resultado == True,"A criação da tabela deveria retornar True"

    def test_inserir_cliente(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente() 
        usuario_base = Usuario(
            id=0, nome="Cliente Teste", email="cliente@teste.com",
            senha="123", cpf_cnpj="789789", telefone="789789",
            data_cadastro=datetime.now(), endereco="Rua do Cliente", tipo_usuario="Cliente"
        )
        id_usuario_criado = inserir_usuario(usuario_base)
        assert id_usuario_criado is not None, "Falha ao criar o usuário base."

        cliente_para_inserir = Cliente(
            id=0,
            id_usuario=id_usuario_criado,
            genero="Feminino",
            data_nascimento=date(1990, 5, 20)
        )
        #Act
        # Assert
        id_cliente_inserido = inserir_cliente(cliente_para_inserir)
        assert id_cliente_inserido is not None and id_cliente_inserido > 0
        with pytest.raises(sqlite3.IntegrityError) as e:
            inserir_cliente(cliente_para_inserir)
        assert "UNIQUE constraint failed" in str(e.value)
    
    def test_obter_todos_os_clientes(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()

        usuario_cliente1 = Usuario(id=0, nome="Cliente Ana", email="ana@cliente.com", senha="123", cpf_cnpj="111", telefone="111", data_cadastro=datetime.now(), endereco="Rua A", tipo_usuario="Cliente")
        usuario_admin = Usuario(id=0, nome="Admin Beto", email="beto@admin.com", senha="123", cpf_cnpj="222", telefone="222", data_cadastro=datetime.now(), endereco="Rua B", tipo_usuario="Administrador")
        usuario_cliente2 = Usuario(id=0, nome="Cliente Carlos", email="carlos@cliente.com", senha="123", cpf_cnpj="333", telefone="333", data_cadastro=datetime.now(), endereco="Rua C", tipo_usuario="Cliente")

        id_ana = inserir_usuario(usuario_cliente1)
        id_beto = inserir_usuario(usuario_admin) # Beto é admin, não cliente. Ele não deve aparecer na lista de clientes.
        id_carlos = inserir_usuario(usuario_cliente2)

        inserir_cliente(Cliente(id=0, id_usuario=id_ana, genero="Feminino", data_nascimento=date(1995, 1, 1)))
        inserir_cliente(Cliente(id=0, id_usuario=id_carlos, genero="Masculino", data_nascimento=date(1992, 2, 2)))
        #Act
        lista_de_clientes = obter_cliente()
        #Assert 
        assert len(lista_de_clientes) == 2
        nomes_encontrados = {cliente.nome for cliente in lista_de_clientes}
        assert "Cliente Ana" in nomes_encontrados
        assert "Cliente Carlos" in nomes_encontrados
        assert "Admin Beto" not in nomes_encontrados


    def test_obter_cliente_por_id(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()

        email_unico = "final@cliente.com"
        usuario_original = Usuario(id=0, nome="Cliente Final", email=email_unico, senha="final123", cpf_cnpj="123123", telefone="123123", data_cadastro=datetime.now(), endereco="Rua Final", tipo_usuario="Cliente")
        id_usuario = inserir_usuario(usuario_original)

        cliente_a_inserir = Cliente(id=0, id_usuario=id_usuario, genero="Masculino", data_nascimento=date(1995, 5, 5))
        id_cliente = inserir_cliente(cliente_a_inserir)
        assert id_cliente is not None, "Falha ao inserir na tabela cliente para o teste."
        #Act
        usuario_encontrado = obter_cliente_por_id(id_cliente)
        #Assert 
        assert usuario_encontrado is not None
        assert isinstance(usuario_encontrado, Usuario)
        assert usuario_encontrado.id == id_usuario
        assert usuario_encontrado.nome == "Cliente Final"

    #criar teste para atualizar cliente

    def test_deletar_um_cliente_e_confirmar_remocao(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        usuario = Usuario(
            id=0, nome="Cliente a ser Excluído", email="excluir@teste.com",
            senha="123", cpf_cnpj="121212", telefone="121212",
            data_cadastro=datetime.now(), endereco="Rua a ser Deletada", tipo_usuario="Cliente"
        )
        id_usuario = inserir_usuario(usuario)
        
        cliente_para_deletar = Cliente(
            id=0, id_usuario=id_usuario, genero="N/A", data_nascimento=date(1970, 1, 1)
        )
        id_cliente_criado = inserir_cliente(cliente_para_deletar)
        
        assert id_cliente_criado is not None, "Falha ao criar o cliente para o teste de deleção."
        #Act
        resultado_delecao = deletar_cliente(cliente_id=id_cliente_criado)
        #assert
        assert resultado_delecao is True, "A função de deletar deveria retornar True."
        try:
            novo_id_cliente = inserir_cliente(cliente_para_deletar)
            assert novo_id_cliente is not None and novo_id_cliente > id_cliente_criado
        except Exception as e:
            assert False, f"A reinserção dos dados do cliente deveria ter sucesso, mas falhou. Erro: {e}"


    