


import sys
import os

from data.fornecedor.fornecedor_repo import criar_tabela_fornecedor
from data.inscricaoplano.inscricao_plano_repo import *
from data.plano.plano_repo import criar_tabela_plano
from data.prestador.prestador_repo import criar_tabela_prestador

class Test_InscricaoPlanoRepo:
    def test_criar_tabela_inscricao_plano(self, test_db):
        #Arrange
        criar_tabela_plano()
        criar_tabela_prestador()
        criar_tabela_fornecedor()
        #Act
        resultado = criar_tabela_inscricao_plano()
        #Assert
        assert resultado == True,"A criação da tabela deveria retornar True"

    def test_inserir_inscricao_plano(self, test_db):
        # Arrange
        criar_tabela_plano()
        criar_tabela_prestador()
        criar_tabela_fornecedor()

        # Suponha que esses IDs foram inseridos antes
        id_fornecedor = 1
        id_prestador = 2
        id_plano = 3
        inscricao_plano_teste = InscricaoPlano(0, id_fornecedor, id_prestador, id_plano)
        # Act
        id_inscricao = inserir_inscricao_plano(inscricao_plano_teste)
        # Assert
        assert id_inscricao is not None
        inscricao_plano_db = inserir_inscricao_plano(id_inscricao)
        assert inscricao_plano_db is not None
        assert inscricao_plano_db.id_fornecedor == id_fornecedor
        assert inscricao_plano_db.id_prestador == id_prestador
        assert inscricao_plano_db.id_plano == id_plano


    def test_obter_inscricao_plano(self, test_db):
            # Arrange
            criar_tabela_plano()
            criar_tabela_prestador()
            criar_tabela_fornecedor()

            email_unico = "email_unico_para_teste@email.com"
            usuario_teste = Usuario(0, "Usuario Unico", email_unico, "senha", "11122233344", "77777777777", datetime.now(), "Endereco Unico")
            inserir_usuario(usuario_teste)
            # Act
            usuario_db = obter_usuario_por_email(email_unico)
            # Assert
            assert usuario_db is not None, "Deveria ter encontrado um usuário com o email especificado"
            assert usuario_db.email == email_unico

    def test_obter_usuario_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        email_unico = "id_test@email.com"
        usuario_original = Usuario(
            id=0,
            nome="Usuario ID Test",
            email=email_unico,
            senha="senha_id",
            cpf_cnpj="55544433322",
            telefone="11222334455",
            data_cadastro=datetime.now(),
            endereco="Endereco Teste ID"
        )
        id_inserido = inserir_usuario(usuario_original)
        # Act
        usuario_encontrado = obter_usuario_por_id(id_inserido)
        # Assert
        assert usuario_encontrado is not None, "A busca por ID não deveria retornar None"
        assert usuario_encontrado.id == id_inserido, "O ID do usuário encontrado não corresponde ao ID inserido"
        assert usuario_encontrado.email == email_unico, "O email do usuário encontrado não corresponde ao original"
        assert usuario_encontrado.nome == "Usuario ID Test", "O nome do usuário encontrado não corresponde ao original"

    def test_atualizar_usuario(self, test_db):
        #Arrange
        criar_tabela_usuario()
        usuario_teste = Usuario(0,"Usuario Teste", "email", "senha", "12345678901", "99999999999", "2023-10-01 12:00:00", "Endereco Teste")
        id_usuario_inserido = inserir_usuario(usuario_teste)
        usuario_inserido = obter_usuario_por_id(id_usuario_inserido)
        #Act
        usuario_inserido.nome = "Usuario Atualizado"
        resultado = atualizar_usuario(usuario_inserido)
        #Assert
        assert resultado == True, "A alteração do usuário deveria retornar True"
        usuario_db = obter_usuario_por_id(id_usuario_inserido)
        assert usuario_db.nome == "Usuario Atualizado", "O nome do usuário alterado não confere"
