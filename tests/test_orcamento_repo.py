from datetime import datetime, timedelta
from data.fornecedor.fornecedor_model import Fornecedor
from data.cliente.cliente_model import Cliente
from data.orcamento.orcamento_model import Orcamento
from data.fornecedor.fornecedor_repo import inserir_fornecedor, criar_tabela_fornecedor
from data.cliente.cliente_repo import inserir_cliente, criar_tabela_cliente
from data.orcamento.orcamento_repo import inserir_orcamento, criar_tabela_orcamento, obter_orcamento_por_id, obter_todos_orcamentos
from data.usuario.usuario_repo import criar_tabela_usuario


class Test_OrcamentoRepo:

    def test_criar_tabela_orcamento(self, test_db):
        criar_tabela_fornecedor()
        criar_tabela_cliente()

        resultado = criar_tabela_orcamento()
        assert resultado is None or resultado == True, "A criação da tabela deveria retornar True ou None"

    def test_inserir_orcamento(self, test_db):
        criar_tabela_usuario()
        criar_tabela_fornecedor()
        criar_tabela_cliente()
        criar_tabela_orcamento()

        fornecedor = Fornecedor(
            0, "Fornecedor Teste", "Fornecedor LTDA", "12345678000199",
            "fornecedor@teste.com", "27999999999", "Rua dos Fornecedores",
            "100", "Centro", "Obratto"
        )
        id_fornecedor = inserir_fornecedor(fornecedor)
        assert id_fornecedor is not None, "Fornecedor não inserido"

        cliente = Cliente(
            0,
            "Cliente Teste",
            "cliente@email.com",
            "senha123",
            "12345678900",
            "27988887777",
            datetime.now(),
            "Rua do Cliente, 123",
            "cliente",
            "feminino",
            datetime(2000, 1, 1)
        )
        id_cliente = inserir_cliente(cliente)
        assert id_cliente is not None, "Cliente não inserido"

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
        criar_tabela_usuario()
        criar_tabela_fornecedor()
        criar_tabela_cliente()
        criar_tabela_orcamento()

        fornecedor = Fornecedor(
            0, "Fornecedor Teste", "Fornecedor LTDA", "12345678000199",
            "fornecedor@teste.com", "27999999999", "Rua dos Fornecedores",
            "100", "Centro", "Obratto"
        )
        id_fornecedor = inserir_fornecedor(fornecedor)
        assert id_fornecedor is not None, "Fornecedor não inserido"

        cliente = Cliente(
            0,
            "Cliente Teste",
            "cliente@email.com",
            "senha123",
            "12345678900",
            "27988887777",
            datetime.now(),
            "Rua do Cliente, 123",
            "cliente",
            "feminino",
            datetime(2000, 1, 1)
        )
        id_cliente = inserir_cliente(cliente)
        assert id_cliente is not None, "Cliente não inserido"

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

        orcamento_obtido = obter_orcamento_por_id(id_orcamento)
        assert orcamento_obtido is not None, "Orçamento não encontrado pelo ID"
        assert orcamento_obtido.id_orcamento == id_orcamento
        assert orcamento_obtido.id_fornecedor == id_fornecedor
        assert orcamento_obtido.id_cliente == id_cliente
        assert orcamento_obtido.valor_estimado == 1500.00
        assert orcamento_obtido.status == "Pendente"
        assert orcamento_obtido.descricao == "Serviço de pintura"

    def test_obter_todos_orcamentos(self, test_db):
        criar_tabela_usuario()
        criar_tabela_fornecedor()
        criar_tabela_cliente()
        criar_tabela_orcamento()

        fornecedor = Fornecedor(
            0, "Fornecedor Teste", "Fornecedor LTDA", "12345678000199",
            "fornecedor@teste.com", "27999999999", "Rua dos Fornecedores",
            "100", "Centro", "Obratto"
        )
        id_fornecedor = inserir_fornecedor(fornecedor)
        assert id_fornecedor is not None, "Fornecedor não inserido"

        cliente = Cliente(
            0,
            "Cliente Teste",
            "cliente@email.com",
            "senha123",
            "12345678900",
            "27988887777",
            datetime.now(),
            "Rua do Cliente, 123",
            "cliente",
            "feminino",
            datetime(2000, 1, 1)
        )
        id_cliente = inserir_cliente(cliente)
        assert id_cliente is not None, "Cliente não inserido"

        orcamento1 = Orcamento(
            id_fornecedor=id_fornecedor,
            id_cliente=id_cliente,
            valor_estimado=1500.00,
            data_solicitacao=datetime.now(),
            prazo_entrega=datetime.now() + timedelta(days=7),
            status="Pendente",
            descricao="Serviço de pintura"
        )
        id_orcamento1 = inserir_orcamento(orcamento1)
        assert id_orcamento1 is not None, "Orçamento 1 não foi inserido com sucesso"

        orcamento2 = Orcamento(
            id_fornecedor=id_fornecedor,
            id_cliente=id_cliente,
            valor_estimado=2500.00,
            data_solicitacao=datetime.now(),
            prazo_entrega=datetime.now() + timedelta(days=10),
            status="Aprovado",
            descricao="Serviço de reforma"
        )
        id_orcamento2 = inserir_orcamento(orcamento2)
        assert id_orcamento2 is not None, "Orçamento 2 não foi inserido com sucesso"

        orcamentos = obter_todos_orcamentos()
        assert isinstance(orcamentos, list)
        assert len(orcamentos) >= 2

        ids = [o.id_orcamento for o in orcamentos]
        assert id_orcamento1 in ids
        assert id_orcamento2 in ids


    def test_atualizar_orcamento_por_id(self, test_db):
        criar_tabela_usuario()
        criar_tabela_fornecedor()
        criar_tabela_cliente()
        criar_tabela_orcamento()

        fornecedor = Fornecedor(
            0, "Fornecedor Teste", "Fornecedor LTDA", "12345678000199",
            "fornecedor@teste.com", "27999999999", "Rua dos Fornecedores",
            "100", "Centro", "Obratto"
        )
        id_fornecedor = inserir_fornecedor(fornecedor)
        assert id_fornecedor is not None

        cliente = Cliente(
            0,
            "Cliente Teste",
            "cliente@email.com",
            "senha123",
            "12345678900",
            "27988887777",
            datetime.now(),
            "Rua do Cliente, 123",
            "cliente",
            "feminino",
            datetime(2000, 1, 1)
        )
        id_cliente = inserir_cliente(cliente)
        assert id_cliente is not None

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
        assert id_orcamento is not None

        orcamento_atualizado = Orcamento(
            id_fornecedor=id_fornecedor,
            id_cliente=id_cliente,
            valor_estimado=2000.00,
            data_solicitacao=orcamento.data_solicitacao,
            prazo_entrega=orcamento.prazo_entrega + timedelta(days=3),
            status="Aprovado",
            descricao="Serviço de pintura atualizado"
        )
        resultado = atualizar_orcamento_por_id(id_orcamento, orcamento_atualizado)
        assert resultado is True

        orcamento_busca = obter_orcamento_por_id(id_orcamento)
        assert orcamento_busca is not None
        assert orcamento_busca.valor_estimado == 2000.00
        assert orcamento_busca.status == "Aprovado"
        assert orcamento_busca.descricao == "Serviço de pintura atualizado"

    def test_deletar_orcamento(self, test_db):
        criar_tabela_usuario()
        criar_tabela_fornecedor()
        criar_tabela_cliente()
        criar_tabela_orcamento()

        fornecedor = Fornecedor(
            0, "Fornecedor Teste", "Fornecedor LTDA", "12345678000199",
            "fornecedor@teste.com", "27999999999", "Rua dos Fornecedores",
            "100", "Centro", "Obratto"
        )
        id_fornecedor = inserir_fornecedor(fornecedor)
        assert id_fornecedor is not None

        cliente = Cliente(
            0,
            "Cliente Teste",
            "cliente@email.com",
            "senha123",
            "12345678900",
            "27988887777",
            datetime.now(),
            "Rua do Cliente, 123",
            "cliente",
            "feminino",
            datetime(2000, 1, 1)
        )
        id_cliente = inserir_cliente(cliente)
        assert id_cliente is not None

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
        assert id_orcamento is not None

        resultado = deletar_orcamento(id_orcamento)
        assert resultado is True

        orcamento_excluido = obter_orcamento_por_id(id_orcamento)
        assert orcamento_excluido is None
