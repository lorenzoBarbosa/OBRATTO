


import sys
import os

from data.fornecedor.fornecedor_model import Fornecedor
from data.fornecedor.fornecedor_repo import criar_tabela_fornecedor
from data.inscricaoplano.inscricao_plano_repo import *
from data.plano.plano_repo import criar_tabela_plano, inserir_plano
from data.prestador.prestador_model import Prestador
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

    def test_obter_inscricao_plano_por_id(self, test_db):
            criar_tabela_plano()
            criar_tabela_prestador()
            criar_tabela_fornecedor()
     
            inscricao_plano = InscricaoPlano(0, 0, 0)
            id_plano = inserir_plano(id_plano)
            prestador = Prestador (0, "", "", "", "", "", "", "", "", "", "", "")
            id_prestador = id_prestador()
            fornecedor = Fornecedor(0,"","","","","","","", "Obratto")
            id_fornecedor = id_fornecedor(id_fornecedor, id_plano)
            inscricaoplano = InscricaoPlano(0, 0, 0)
            # Act fazer a ação que será testada
            id_plano = inserir_plano(plano)
            id_prestador = inserir_prestador(prestador)
            id_fornecedor = inserir_fornecedor(fornecedor)
            inscricao_plano_db = obter_inscricao_plano_por_id()
    # Asserts verificar se o resultado é o esperado
            assert id_plano is not None, "O anúncio não foi inserido com sucesso."
            assert id_prestador is not None, "O anúncio não foi inserido com sucesso."
            assert id_fornecedor is not None, "O anúncio não foi inserido com sucesso."


    def test_atualizar_inscricao_plano(self, test_db):
        #Arrange
        criar_tabela_plano()
        criar_tabela_prestador()
        criar_tabela_fornecedor()
        