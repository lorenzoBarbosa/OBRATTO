from datetime import datetime, date, timedelta
import pytest

from data.usuario.usuario_model import Usuario
from data.usuario.usuario_repo import criar_tabela_usuario, inserir_usuario

from data.fornecedor.fornecedor_model import Fornecedor
from data.fornecedor.fornecedor_repo import criar_tabela_fornecedor, inserir_fornecedor

from data.cliente.cliente_model import Cliente
from data.cliente.cliente_repo import criar_tabela_cliente, inserir_cliente

from data.orcamento.orcamento_model import Orcamento
from data.orcamento.orcamento_repo import criar_tabela_orcamento, deletar_orcamento, inserir_orcamento, obter_orcamento_por_id, obter_todos_orcamentos

from datetime import datetime, timedelta, date
from data.orcamento.orcamento_model import Orcamento


class Test_OrcamentoRepo:
    def test_criar_tabela_orcamento(self, test_db):
        criar_tabela_usuario()  # Garantir que usuário existe, se necessário
        criar_tabela_fornecedor()
        criar_tabela_cliente()
        resultado = criar_tabela_orcamento()
        assert resultado is True, "A criação da tabela deveria retornar True"

    def test_inserir_orcamento(self, test_db):
        # Criar todas as tabelas necessárias
        criar_tabela_usuario()
        criar_tabela_fornecedor()
        criar_tabela_cliente()
        criar_tabela_orcamento()

        # Criar e inserir usuário fornecedor
        usuario_fornecedor = Usuario(
            id=0,
            nome="Fornecedor Teste",
            email="fornecedor@teste.com",
            senha="senha123",
            cpf_cnpj="12345678000199",
            telefone="27999999999",
            data_cadastro=datetime.now(),
            endereco="Rua dos Fornecedores",
            tipo_usuario="Fornecedor"
        )
        id_usuario_fornecedor = inserir_usuario(usuario_fornecedor)
        assert id_usuario_fornecedor is not None, "Usuário fornecedor não inserido"

        # Criar e inserir fornecedor (herdando dados do usuário)
        fornecedor = Fornecedor(
            id=0,
            nome="Fornecedor Teste",
            email="fornecedor@teste.com",
            senha="senha123",
            cpf_cnpj="12345678000199",
            telefone="27999999999",
            data_cadastro=datetime.now(),
            endereco="Rua dos Fornecedores",
            tipo_usuario="Fornecedor",
            razao_social="Fornecedor LTDA"
        )
        id_fornecedor = inserir_fornecedor(fornecedor)
        assert id_fornecedor is not None, "Fornecedor não inserido"

        # Criar e inserir usuário cliente
        usuario_cliente = Usuario(
            id=0,
            nome="Cliente Teste",
            email="cliente@email.com",
            senha="senha123",
            cpf_cnpj="12345678900",
            telefone="27988887777",
            data_cadastro=datetime.now(),
            endereco="Rua do Cliente, 123",
            tipo_usuario="Cliente"
        )
        id_usuario_cliente = inserir_usuario(usuario_cliente)
        assert id_usuario_cliente is not None, "Usuário cliente não inserido"

        # Criar e inserir cliente (com FK para usuário)
        cliente = Cliente(
            id=0,
            id_usuario=id_usuario_cliente,
            genero="feminino",
            data_nascimento=date(2000, 1, 1)
        )
        id_cliente = inserir_cliente(cliente)
        assert id_cliente is not None, "Cliente não inserido"

        # Criar e inserir orçamento
        orcamento = Orcamento(
            id_fornecedor=id_fornecedor,
            id_cliente=id_cliente,
            valor_estimado=1500.00,
            data_solicitacao=datetime.now(),
            prazo_entrega=datetime.now() + timedelta(days=7),
            status="Pendente",
            descricao="Serviço de pintura"
        )
        id_orcamento = inserir_orcamento(orcamento)
        assert id_orcamento is not None, "Orçamento não foi inserido com sucesso"

    def test_obter_orcamento_por_id(self, test_db):
        # Teste parecido com o anterior, para obter orçamento pelo id
        # ... (aqui você pode seguir o padrão do test_inserir_orcamento)
        pass

    def test_atualizar_orcamento_por_id(self, test_db):
        criar_tabela_usuario()
        criar_tabela_fornecedor()
        criar_tabela_cliente()
        criar_tabela_orcamento()

        # Cadastrar usuário/fornecedor
        usuario_f = Usuario(
            id=0, nome="F", email="f@f.com", senha="1", cpf_cnpj="1", telefone="1",
            data_cadastro=datetime.now(), endereco="End", tipo_usuario="Fornecedor"
        )
        id_usuario_f = inserir_usuario(usuario_f)
        fornecedor = Fornecedor(
            id=0, nome="F", email="f@f.com", senha="1", cpf_cnpj="1", telefone="1",
            data_cadastro=datetime.now(), endereco="End", tipo_usuario="Fornecedor", razao_social="F LTDA"
        )
        id_fornecedor = inserir_fornecedor(fornecedor)

        # Cliente
        usuario_c = Usuario(
            id=0, nome="C", email="c@c.com", senha="2", cpf_cnpj="2", telefone="2",
            data_cadastro=datetime.now(), endereco="End", tipo_usuario="Cliente"
        )
        id_usuario_c = inserir_usuario(usuario_c)
        cliente = Cliente(
            id=0, id_usuario=id_usuario_c, genero="Feminino", data_nascimento=date(2000, 1, 1)
        )
        id_cliente = inserir_cliente(cliente)

        orcamento = Orcamento(
            id_fornecedor=id_fornecedor,
            id_cliente=id_cliente,
            valor_estimado=1000,
            data_solicitacao=datetime.now(),
            prazo_entrega=datetime.now() + timedelta(days=3),
            status="Pendente",
            descricao="..."
        )

        # INSERIR O ORÇAMENTO ORIGINAL E GUARDAR O ID
        id_orcamento = inserir_orcamento(orcamento)

        orcamento_atualizado = Orcamento(
            id=id_orcamento,
            id_fornecedor=id_fornecedor,
            id_cliente=id_cliente,
            valor_estimado=1200,
            data_solicitacao=orcamento.data_solicitacao,
            prazo_entrega=datetime.now() + timedelta(days=2),
            status="Aprovado",
            descricao="Atualizado"
        )
        from data.orcamento.orcamento_repo import atualizar_orcamento
        sucesso = atualizar_orcamento(orcamento_atualizado)
        assert sucesso is True

        atualizado = obter_orcamento_por_id(id_orcamento)
        assert atualizado.valor_estimado == 1200.0
        assert atualizado.status == "Aprovado"
        assert "atualizada" in atualizado.descricao

    def test_deletar_orcamento(self, test_db):
        criar_tabela_orcamento()

        orcamento = Orcamento(
            id_fornecedor=5,
            id_cliente=6,
            valor_estimado=4000,
            data_solicitacao=datetime.datetime.now(),
            prazo_entrega=datetime.now() + timedelta(days=10),
            status="Cancelado",
            descricao="Orçamento a deletar"
        )
        id_orc = inserir_orcamento(orcamento)

        sucesso = deletar_orcamento(id_orc)
        assert sucesso is True

        orc_db = obter_orcamento_por_id(id_orc)
        assert orc_db is None


   