from asyncio import open_connection as async_open_connection
from utils.db import open_connection
import pytest
from datetime import datetime
from data.cliente.cliente_model import Cliente
from data.cliente.cliente_repo import criar_tabela_cliente, inserir_cliente
from data.fornecedor.fornecedor_repo import criar_tabela_fornecedor
from data.prestador.prestador_model import Prestador
from data.prestador.prestador_repo import criar_tabela_prestador, inserir_prestador
from data.avaliacao.avaliacao_model import Avaliacao
from data.avaliacao.avaliacao_repo import (
    criar_tabela_avaliacao,
    inserir_avaliacao,
    obter_todos,
    obter_avaliacao_por_id,
    atualizar_avaliacao,
    deletar_avaliacao
)
from data.usuario.usuario_repo import criar_tabela_usuario, inserir_usuario
from data.usuario.usuario_model import Usuario


class TestAvaliacaoRepo:

    def test_criar_tabela_avaliacao(self):
        #Arrange
        criar_tabela_usuario()
        #Act
        resultado = criar_tabela_avaliacao()
        #Assert
        assert resultado is True

    def inserir_avaliacao_para_teste(self) -> int:
        usuario_avaliador = Usuario(
            id=0,
            nome="Avaliador",
            email="avaliador@teste.com",
            senha="123",
            cpf_cnpj="11111111111",
            telefone="11999999999",
            data_cadastro=datetime.now().isoformat(),
            endereco="Rua A, 123",
            tipo_usuario="cliente"
        )
        id_usuario_avaliador = inserir_usuario(usuario_avaliador)

        cliente = Cliente(
            id=0,
            id_usuario=id_usuario_avaliador,
            genero="Feminino",
            data_nascimento=datetime.strptime("2000-01-01", "%Y-%m-%d").date()
        )
        id_cliente = inserir_cliente(cliente)
        cliente.id = id_cliente

        usuario_prestador = Usuario(
            id=0,
            nome="Avaliado",
            email="avaliado@teste.com",
            senha="123",
            cpf_cnpj="22222222222",
            telefone="11999999999",
            data_cadastro=datetime.now().isoformat(),
            endereco="Rua B, 456",
            tipo_usuario="prestador"
        )
        id_usuario_prestador = inserir_usuario(usuario_prestador)

        prestador = Prestador(
            id=id_usuario_prestador,
            nome="Avaliado",
            email="avaliado@teste.com",
            senha="123",
            cpf_cnpj="22222222222",
            telefone="11999999999",
            endereco="Rua B, 456",
            tipo_usuario="prestador",
            data_cadastro=datetime.now().isoformat(),
            area_atuacao="Limpeza",
            tipo_pessoa="Física",
            razao_social="Avaliado Prestador",
            descricao_servicos="Serviço de limpeza"
        )

        id_prestador = inserir_prestador(prestador)
        prestador.id = id_prestador

        avaliacao = Avaliacao(
            id_avaliacao=0,
            id_avaliador=id_cliente,
            id_avaliado=id_prestador,
            nota=4.5,
            data_avaliacao=datetime.now(),
            descricao="Excelente trabalho!"
        )
        id_avaliacao = inserir_avaliacao(avaliacao)

        return id_avaliacao

    def test_inserir_avaliacao(self, test_db):
        #Arrange

        criar_tabela_usuario()
        criar_tabela_avaliacao()
        criar_tabela_cliente()
        criar_tabela_fornecedor()
        criar_tabela_prestador()

        #Act
        usuario1 = Usuario(
            id=0,
            nome="Avaliador",
            email="a@a.com",
            senha="123",
            cpf_cnpj="12345678900",
            telefone="11999999999",
            data_cadastro=datetime.now().isoformat(),
            endereco="Rua A, 123",
            tipo_usuario="cliente"
        )

        usuario2 = Usuario(
            id=0,
            nome="Avaliado",
            email="b@b.com",
            senha="123",
            cpf_cnpj="98765432100",
            telefone="21999999999",
            data_cadastro=datetime.now().isoformat(),
            endereco="Rua B, 456",
            tipo_usuario="fornecedor"
        )
        id1 = inserir_usuario(usuario1)
        id2 = inserir_usuario(usuario2)

        avaliacao = Avaliacao(
            id_avaliacao=0,
            id_avaliador=1,
            id_avaliado=2,
            nota=5.0,
            data_avaliacao=datetime.now(),
            descricao="Excelente!"
        )

        id_avaliacao = inserir_avaliacao(avaliacao)
        avaliacao_db = obter_avaliacao_por_id(id_avaliacao)
        #Assert
        assert avaliacao_db is not None

    def test_obter_avaliacao(self, test_db):

        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS cliente")
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS fornecedor")
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS prestador")    
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS usuario")

        #Arrange
        criar_tabela_usuario()
        criar_tabela_avaliacao()
        criar_tabela_cliente()
        criar_tabela_fornecedor()
        criar_tabela_prestador()

        #Act
        id_avaliacao = self.inserir_avaliacao_para_teste()
        avaliacoes = obter_todos()

        for a in avaliacoes:
            print("↪ id_avaliacao:", a.id_avaliacao)
        #Assert
        assert any(a.id_avaliacao == id_avaliacao for a in avaliacoes)

    def test_obter_avaliacao_por_id(self, test_db):
        
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS cliente")
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS fornecedor")
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS prestador")    
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS usuario")

        #Arrange
        criar_tabela_usuario()
        criar_tabela_avaliacao()
        criar_tabela_cliente()
        criar_tabela_fornecedor()
        criar_tabela_prestador()
        #Act
        id_avaliacao = self.inserir_avaliacao_para_teste()
        avaliacao_db = obter_avaliacao_por_id(id_avaliacao)
        #Assert
        assert avaliacao_db is not None
        assert isinstance(avaliacao_db.descricao, str)

    def test_atualizar_avaliacao(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_avaliacao()
        criar_tabela_cliente()
        criar_tabela_fornecedor()
        criar_tabela_prestador()

        #Act
        id_avaliacao = self.inserir_avaliacao_para_teste()
        avaliacao = obter_avaliacao_por_id(id_avaliacao)
        avaliacao.descricao = "Avaliação atualizada"
        resultado = atualizar_avaliacao(avaliacao)
        #Assert
        assert resultado is True

    def test_deletar_avaliacao(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_avaliacao()
        criar_tabela_cliente()
        criar_tabela_fornecedor()
        criar_tabela_prestador()

        #Act
        id_avaliacao = self.inserir_avaliacao_para_teste()
        resultado = deletar_avaliacao(id_avaliacao)
        #Assert
        assert resultado is True

