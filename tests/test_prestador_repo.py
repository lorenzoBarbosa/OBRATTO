from typing import Optional
import pytest
import sqlite3
from datetime import date, datetime
from data.cliente.cliente_repo import criar_tabela_cliente
from utils.db import open_connection


from data.usuario.usuario_model import Usuario
from data.usuario.usuario_repo import criar_tabela_usuario, inserir_usuario

from data.prestador.prestador_model import Prestador
from data.prestador.prestador_repo import*




class TestPrestadorRepo:

    def test_criar_tabela_prestador(self, test_db):
        #Arrange
        #Act
        resultado = criar_tabela_cliente()
        #Assert
        assert resultado == True,"A criação da tabela deveria retornar True"

    def test_inserir_prestador(self, test_db):
        #Arrange 
        criar_tabela_usuario()
        criar_tabela_prestador() 
        usuario_base = Usuario(
            id=0, nome="Marceneiro Zé", email="ze@marceneiro.com",
            senha="123", cpf_cnpj="111.222.333-44", telefone="28999991111",
            data_cadastro=datetime.now(), endereco="Rua da Madeira", tipo_usuario="Prestador"
        )
        id_usuario_criado = inserir_usuario(usuario_base)
        assert id_usuario_criado is not None, "Falha ao criar o usuário base."
        prestador_para_inserir = Prestador(
            id=0,
            id_usuario=id_usuario_criado,
            area_atuacao="Marcenaria",
            tipo_pessoa="Física"
        )
        #Act
        # Assert 
        id_prestador_inserido = inserir_prestador(prestador_para_inserir)
        assert id_prestador_inserido is not None and id_prestador_inserido > 0
        with pytest.raises(sqlite3.IntegrityError) as e:
            inserir_prestador(prestador_para_inserir)
        
        assert "UNIQUE constraint failed" in str(e.value)

    
