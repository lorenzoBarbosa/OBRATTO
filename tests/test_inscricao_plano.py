import sys
import os

from data.fornecedor.fornecedor_model import *
from data.fornecedor.fornecedor_repo import *
from data.inscricaoplano.inscricao_plano_repo import *
from data.plano.plano_model import Plano
from data.plano.plano_repo import *
from data.prestador.prestador_model import Prestador
from data.prestador.prestador_repo import *
from data.usuario.usuario_repo import *

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




    def test_obter_inscricao_plano_por_id(self, test_db):
        criar_tabela_usuario()
        criar_tabela_fornecedor()
        criar_tabela_plano()
        criar_tabela_prestador()
        criar_tabela_inscricao_plano()

        fornecedor = Fornecedor(
            0,
            "Fornecedor Teste",
            "Fornecedor LTDA",  
            "12345678000199",  
            "fornecedor@teste.com",
            "27999999999",
            "Rua dos Fornecedores",
            "100",
            "Centro",
            "Obratto"
    )
        id_fornecedor = inserir_fornecedor(fornecedor)
        assert id_fornecedor is not None, "Fornecedor não foi inserido com sucesso"

        plano = Plano(
            id_plano= 0,
            nome="Plano Básico",
            descricao="Acesso limitado",
            valor_mensal="10",
            limite_servico= "3",
            tipo_plano="gratuito",
            descricao="maquinario"
    )
        id_plano = inserir_plano(plano)
        assert id_plano is not None, "Plano não foi inserido com sucesso"

        prestador = Prestador(
         id=0,
         nome="Maria Prestadora",
         cpf="11122233344",
         email="maria@prestadora.com",
         telefone="27988887777",
         rua="Rua das Prestadoras",
         numero="200",
         bairro="Bairro B",
         cidade="Cidade C",
         estado="ES",
         cep="29000-000",
         senha="senha123"
    )
        id_prestador = inserir_prestador(prestador)
        assert id_prestador is not None, "Prestador não foi inserido com sucesso"

        inscricao = InscricaoPlano(
            id=0,
            id_prestador=id_prestador,
            id_plano=id_plano
    )
        id_inscricao = inserir_inscricao_plano(inscricao)
        assert id_inscricao is not None, "Inscrição de plano não foi inserida com sucesso"

        inscricao_db = obter_inscricao_plano_por_id(id_inscricao)

        assert inscricao_db is not None, "Inscrição de plano não foi encontrada"
        assert inscricao_db.id == id_inscricao
        assert inscricao_db.id_plano == id_plano
        assert inscricao_db.id_prestador == id_prestador